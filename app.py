"""
Career OS - Production Streamlit App
Built for scale, designed for trust
"""

import streamlit as st
import google.generativeai as genai
from pymongo import MongoClient
from datetime import datetime
import json
import os
import hashlib
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

from config import *
from utils import *
from styles import get_custom_css

# Load environment
load_dotenv()

# Configure APIs
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Try multiple models in order of preference
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
    except:
        try:
            model = genai.GenerativeModel('gemini-1.5-pro')
        except:
            model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gemini configuration error: {e}")

# Page config
st.set_page_config(
    page_title="Career OS",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ===================================
# DATABASE & SHEETS SETUP
# ===================================

@st.cache_resource
def get_mongo_client():
    """MongoDB connection"""
    return MongoClient(st.secrets["MONGO_URI"])

def get_sheets_client():
    """Google Sheets connection (silent tracking)"""
    try:
        creds = Credentials.from_service_account_info(
            {
                "type": "service_account",
                "project_id": st.secrets["GOOGLE_PROJECT_ID"],
                "private_key": st.secrets["GOOGLE_PRIVATE_KEY"].replace('\\n', '\n'),
                "client_email": st.secrets["GOOGLE_CLIENT_EMAIL"],
            },
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        client = gspread.authorize(creds)
        return client.open_by_key(st.secrets["GOOGLE_SHEET_ID"]).sheet1
    except:
        return None

# ===================================
# SESSION STATE INITIALIZATION
# ===================================

if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'session_id' not in st.session_state:
    st.session_state.session_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:12]
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'verdict' not in st.session_state:
    st.session_state.verdict = None
if 'resume_verdict' not in st.session_state:
    st.session_state.resume_verdict = None

# ===================================
# DATA PERSISTENCE (SILENT)
# ===================================

def save_assessment_silently(answers, verdict, resume_verdict=None):
    """Save to MongoDB + Sheets without telling user"""
    try:
        # MongoDB
        client = get_mongo_client()
        db = client['career_os']
        
        # Calculate metrics
        comp_gap = ((answers.get('target_comp', 0) - answers.get('current_comp', 1)) / max(answers.get('current_comp', 1), 1)) * 100
        
        record = {
            'session_id': st.session_state.session_id,
            'timestamp': datetime.now(),
            'ip_address': get_client_ip(),
            'user_agent': get_user_agent(),
            'session_duration': (datetime.now() - st.session_state.start_time).total_seconds(),
            
            # User data
            'answers': answers,
            'verdict': verdict,
            'resume_verdict': resume_verdict,
            
            # Derived metrics
            'comp_gap_percent': round(comp_gap, 1),
            'tech_count': len(answers.get('tech_stack', [])),
            'should_switch': verdict.get('verdict') in ['SWITCH_NOW', 'EXPLORE'],
            
            # Metadata
            'source': 'streamlit_v2',
            'version': '2.0'
        }
        
        db.assessments.insert_one(record)
        
        # Google Sheets (silent tracking)
        try:
            sheet = get_sheets_client()
            if sheet:
                row = [
                    datetime.now().isoformat(),
                    st.session_state.session_id,
                    answers.get('career_stage', ''),
                    answers.get('current_comp', 0),
                    answers.get('target_comp', 0),
                    round(comp_gap, 1),
                    ', '.join(answers.get('tech_stack', [])),
                    len(answers.get('tech_stack', [])),
                    answers.get('confidence', 0),
                    answers.get('biggest_fear', ''),
                    answers.get('time_horizon', ''),
                    answers.get('risk_appetite', ''),
                    answers.get('priority', ''),
                    answers.get('company_quality', ''),
                    answers.get('skill_gap', ''),
                    verdict.get('verdict', ''),
                    verdict.get('confidence', 0),
                    1 if verdict.get('verdict') in ['SWITCH_NOW'] else 0,
                    1 if resume_verdict else 0,
                    resume_verdict.get('resume_strength', '') if resume_verdict else '',
                    resume_verdict.get('market_readiness_score', 0) if resume_verdict else 0,
                    get_client_ip(),
                    get_user_agent()[:50],
                    int((datetime.now() - st.session_state.start_time).total_seconds())
                ]
                sheet.append_row(row)
        except Exception as e:
            print(f"Sheets error: {e}")
            pass  # Silent fail - never show errors to user
            
        return True
    except Exception as e:
        # Log but don't fail
        print(f"Silent save failed: {e}")
        return False

# ===================================
# AI FUNCTIONS
# ===================================

def get_career_verdict(answers):
    """Get AI career recommendation"""
    
    prompt = f"""You are Career OS — an AI career advisor for early-career tech professionals.

CORE PRINCIPLES:
-Do not stay harsh about service based companies and any other company 
-Maximum users are freshers so advice according to indian market conditions 
- 60% direct and realistic, 40% supportive and encouraging
- Honest about challenges BUT also recognize their strengths
- Call out issues clearly BUT frame them as fixable problems
- Be real, not scary - people are trying their best
- Like a supportive senior who tells you the truth but has your back
-Do not give quick switching advice 
- Optimize for long-term career leverage, NOT short-term money
- Be blunt and realistic about market dynamics
- Call out bad decisions clearly
- No motivational fluff or generic platitudes
-Be real stay little strict and soft at the same time 
-Do not halucinate 
-Be like a big brother guiding 

TONE: Direct, mentor-like, professional but honest

---

ANALYZE THIS PROFILE:

Situation: {answers['career_stage']}
Current: ₹{answers.get('current_comp', 0):,} → Target: ₹{answers.get('target_comp', 0):,}
Gap: {((answers.get('target_comp', 0) - answers.get('current_comp', 1)) / max(answers.get('current_comp', 1), 1) * 100):.0f}%

Tech Stack: {', '.join(answers['tech_stack'])}
Self-Rating: {answers['confidence']}/5
Biggest Fear: {answers['biggest_fear']}
Timeline: {answers['time_horizon']}
Risk Profile: {answers['risk_appetite']}
Priority: {answers['priority']}
Company: {answers['company_quality']}
Weakness: {answers['skill_gap']}

RESPOND WITH VALID JSON ONLY (no markdown, no backticks):

{{
  "verdict": "SWITCH_NOW",
  "confidence": 0.85,
  "one_line": "Brutal one-line summary",
  "why": ["Reason 1", "Reason 2", "Reason 3"],
  "risks_if_ignored": ["Risk 1", "Risk 2"],
  "90_day_plan": ["Week 1-4: Action", "Week 5-8: Action", "Week 9-12: Action"],
  "harsh_truth": "One uncomfortable reality they need to hear"
}}

VERDICT OPTIONS: SWITCH_NOW | BUILD_THEN_SWITCH | WAIT | PIVOT_STACK"""

    try:
        # Try with safety settings to avoid blocks
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        
        # Generate content with better error handling
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                top_k=40,
                max_output_tokens=20000,
            )
        )
        
        # Check if response was blocked
        if not response.text:
            st.error("Response was blocked by safety filters")
            st.write("Prompt feedback:", response.prompt_feedback)
            return None
        
        # Get text
        raw_text = response.text
        
        # Clean response
        text = raw_text.replace('```json', '').replace('```', '').strip()
        
        # Parse JSON
        verdict = json.loads(text)
        
        # Validate required fields
        required_fields = ['verdict', 'confidence', 'one_line', 'why', 'risks_if_ignored', '90_day_plan', 'harsh_truth']
        for field in required_fields:
            if field not in verdict:
                st.error(f"Missing field in response: {field}")
                return None
        
        return verdict
        
    except json.JSONDecodeError as e:
        st.error(f"❌ JSON Parse Error: {e}")
        if 'raw_text' in locals():
            st.code(raw_text[:500], language='text')
        return None
        
    except Exception as e:
        error_msg = str(e)
        st.error(f"❌ Gemini API Error: {error_msg}")
        
        # Common error types
        if "quota" in error_msg.lower():
            st.error("⚠️ API quota exceeded. Please wait a few minutes and try again.")
        elif "api key" in error_msg.lower():
            st.error("⚠️ API key issue. Check your Streamlit secrets.")
        elif "model" in error_msg.lower():
            st.error("⚠️ Model not available. Try using gemini-1.5-pro instead.")
        else:
            st.error(f"Error type: {type(e).__name__}")
            
        return None

def analyze_resume(file_content):
    """Analyze uploaded resume"""
    
    prompt = f"""{RESUME_SYSTEM_PROMPT}

Analyze this resume for Indian tech market competitiveness.
-Be real and a little strict 
-We are to help people not sugercoat 
-Read it completely and do not halucinate
-Do not go anything beyond resume like  a second-year student etc etc
RESUME TEXT:
{file_content[:4000]}

RESPOND WITH VALID JSON:

{{
  "resume_strength": "Weak | Average | Strong",
  "market_readiness_score": 65,
  "first_impression": "What recruiter thinks in 10 seconds",
  "red_flags": ["Flag 1", "Flag 2"],
  "strengths": ["Strength 1"],
  "quick_fixes": ["Fix 1", "Fix 2", "Fix 3"],
  "hireability": "Low | Medium | High"
}}"""

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=20000,
            )
        )
        
        raw_text = response.text
        text = raw_text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
        
    except Exception as e:
        st.error(f"Resume analysis error: {str(e)}")
        return None

# ===================================
# PAGE: LANDING
# ===================================

if st.session_state.page == 'landing':
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown("# Most engineers ruin their career by switching too early.")
    st.markdown("### Career OS tells you if you're ready — or if you'll regret it.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Get Your Verdict", type="primary", use_container_width=True):
            st.session_state.page = 'questions'
            st.rerun()
    
    st.markdown("*Takes 2 minutes. Brutally honest. No BS.*")
    
    # Social proof
    st.markdown("---")
    st.markdown("*Trusted by engineers making career decisions*")

# ===================================
# PAGE: QUESTIONS
# ===================================

elif st.session_state.page == 'questions':
    st.markdown("## Quick Assessment")
    st.markdown("*Answer honestly. We'll call out any delusions.*")
    
    with st.form("assessment"):
        answers = {}
        
        for q in QUESTIONS:
            st.markdown(f"### {q['label']}")
            if 'help' in q:
                st.caption(q['help'])
            
            if q['type'] == 'radio':
                answers[q['id']] = st.radio(
                    q['label'],
                    q['options'],
                    label_visibility="collapsed",
                    horizontal=len(q['options']) <= 3
                )
            
            elif q['type'] == 'select':
                answers[q['id']] = st.selectbox(
                    q['label'],
                    q['options'],
                    label_visibility="collapsed"
                )
            
            elif q['type'] == 'multiselect':
                answers[q['id']] = st.multiselect(
                    q['label'],
                    q['options'],
                    label_visibility="collapsed"
                )
            
            elif q['type'] == 'slider':
                answers[q['id']] = st.slider(
                    q['label'],
                    q['min'],
                    q['max'],
                    (q['min'] + q['max']) // 2,
                    label_visibility="collapsed"
                )
            
            elif q['type'] == 'comp_range':
                col1, col2 = st.columns(2)
                with col1:
                    answers['current_comp'] = st.number_input(
                        q['current_label'],
                        min_value=0,
                        value=800000,
                        step=100000
                    )
                with col2:
                    answers['target_comp'] = st.number_input(
                        q['target_label'],
                        min_value=0,
                        value=1200000,
                        step=100000
                    )
            
            st.markdown("<br>", unsafe_allow_html=True)
        
        # Show loading state if processing
        if st.session_state.get('processing', False):
            st.info("⏳ **Processing your assessment... Please wait, do not refresh!**")
        
        submitted = st.form_submit_button(
            "Get My Verdict", 
            type="primary", 
            use_container_width=True,
            disabled=st.session_state.get('processing', False)  # Disable when processing
        )
        
        if submitted:
            # Validation
            if 'tech_stack' in answers and len(answers.get('tech_stack', [])) == 0:
                st.error("Select at least one technology you actually know")
            else:
                # Show immediate feedback
                with st.spinner("⏳ Processing your assessment..."):
                    import time
                    time.sleep(0.5)  # Brief pause to show loading
                    
                    # Set processing flag
                    st.session_state.processing = True
                    st.session_state.answers = answers
                    st.session_state.page = 'processing'
                st.rerun()

# ===================================
# PAGE: PROCESSING
# ===================================

elif st.session_state.page == 'processing':
    st.markdown("## Analyzing Your Profile...")
    
    progress = st.progress(0)
    status = st.empty()
    
    import time
    
    status.text("Reading your answers...")
    progress.progress(20)
    time.sleep(0.5)
    
    status.text("Running AI analysis...")
    progress.progress(50)
    
    verdict = get_career_verdict(st.session_state.answers)
    
    if verdict:
        progress.progress(80)
        status.text("Generating recommendations...")
        time.sleep(0.3)
        
        # Save silently
        save_assessment_silently(st.session_state.answers, verdict)
        
        progress.progress(100)
        st.session_state.verdict = verdict
        st.session_state.processing = False  # Reset processing flag
        st.session_state.page = 'verdict'
        time.sleep(0.5)
        st.rerun()
    else:
        st.session_state.processing = False  # Reset on error too
        st.error("Analysis failed. Please try again.")
        if st.button("Back to Questions"):
            st.session_state.page = 'questions'
            st.rerun()

# ===================================
# PAGE: VERDICT
# ===================================

elif st.session_state.page == 'verdict':
    v = st.session_state.verdict
    
    # Verdict header
    verdict_color = {
        'SWITCH_NOW': '#16a34a',
        'BUILD_THEN_SWITCH': '#ea580c',
        'WAIT': '#dc2626',
        'PIVOT_STACK': '#9333ea'
    }.get(v['verdict'], '#000')
    
    st.markdown(f"""
    <div style='text-align: center; padding: 2rem; background: {verdict_color}15; border-radius: 12px; border-left: 4px solid {verdict_color}; margin-bottom: 2rem;'>
        <h1 style='color: {verdict_color}; margin: 0;'>{v['verdict'].replace('_', ' ')}</h1>
        <p style='font-size: 1.2rem; margin: 0.5rem 0 0 0; color: #666;'>Confidence: {int(v['confidence'] * 100)}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    # One-liner
    st.markdown(f"### {v['one_line']}")
    
    # Why
    st.markdown("#### Why This Verdict")
    for reason in v['why']:
        st.markdown(f"• {reason}")
    
    # Harsh truth
    if 'harsh_truth' in v:
        st.markdown("#### 💊 The Uncomfortable Truth")
        st.warning(v['harsh_truth'])
    
    # Risks
    st.markdown("#### ⚠️ If You Ignore This")
    for risk in v['risks_if_ignored']:
        st.markdown(f"• {risk}")
    
    # Action plan
    st.markdown("#### 🎯 Your 90-Day Plan")
    for i, action in enumerate(v['90_day_plan'], 1):
        st.markdown(f"{i}. {action}")
    
    st.markdown("---")
    
    # Resume upload CTA
    st.markdown("### Want a Resume Reality Check?")
    st.markdown("*Upload your resume to see if it matches your ambitions*")
    
    uploaded = st.file_uploader(
        "Upload Resume (PDF only)",
        type=['pdf'],
        key='resume_uploader',
        label_visibility="collapsed"
    )
    
    if uploaded is not None:
        # Show loading state if processing resume
        if st.session_state.get('processing_resume', False):
            st.info("⏳ **Analyzing your resume... Please wait, do not refresh!**")
        
        # Store the file bytes immediately
        analyze_button = st.button(
            "Analyze Resume", 
            type="primary",
            disabled=st.session_state.get('processing_resume', False)  # Disable when processing
        )
        
        if analyze_button:
            # Show immediate feedback
            with st.spinner("⏳ Processing your resume..."):
                import time
                time.sleep(0.5)
                
                st.session_state.processing_resume = True
                st.session_state.resume_file_bytes = uploaded.read()
                st.session_state.resume_file_name = uploaded.name
                st.session_state.page = 'resume_processing'
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("Start New Assessment"):
        st.session_state.page = 'landing'
        st.session_state.answers = {}
        st.session_state.verdict = None
        st.rerun()

# ===================================
# PAGE: RESUME PROCESSING
# ===================================

elif st.session_state.page == 'resume_processing':
    st.markdown("## Analyzing Resume...")
    st.markdown(f"*Processing: {st.session_state.get('resume_file_name', 'resume.pdf')}*")
    
    try:
        # Extract text from PDF
        import PyPDF2
        import io
        
        # Use the stored bytes
        file_bytes = st.session_state.resume_file_bytes
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        
        st.info(f"📄 PDF has {len(pdf_reader.pages)} page(s)")
        
        resume_text = ""
        for i, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            resume_text += page_text
            st.write(f"✅ Extracted page {i+1}")
        
        st.write(f"📝 Total text length: {len(resume_text)} characters")
        
        if not resume_text or len(resume_text) < 100:
            st.session_state.processing_resume = False  # Reset flag
            st.error("❌ Could not extract enough text from PDF.")
            st.warning("**Possible reasons:**")
            st.markdown("- PDF is image-based (scanned document)")
            st.markdown("- PDF is corrupted")
            st.markdown("- PDF has security restrictions")
            st.markdown("\n**Solution:** Try converting to a text-based PDF using Google Docs or Word")
            
            if st.button("Back to Verdict"):
                st.session_state.page = 'verdict'
                st.rerun()
        else:
            st.success(f"✅ Successfully extracted {len(resume_text)} characters")
            
            with st.spinner("🤖 AI is analyzing your resume..."):
                import time
                time.sleep(1)  # Give user time to see progress
                resume_verdict = analyze_resume(resume_text)
            
            if resume_verdict:
                st.success("✅ Analysis complete!")
                
                # Save with resume
                save_assessment_silently(
                    st.session_state.answers,
                    st.session_state.verdict,
                    resume_verdict
                )
                
                st.session_state.resume_verdict = resume_verdict
                st.session_state.processing_resume = False  # Reset flag
                st.session_state.page = 'resume_verdict'
                time.sleep(0.5)
                st.rerun()
            else:
                st.session_state.processing_resume = False  # Reset on error
                st.error("❌ Resume analysis failed. AI couldn't process the text.")
                if st.button("Back to Verdict"):
                    st.session_state.page = 'verdict'
                    st.rerun()
    
    except Exception as e:
        st.session_state.processing_resume = False  # Reset flag on error
        st.error(f"❌ Error processing PDF: {str(e)}")
        st.code(str(e), language='text')
        st.error("**Please try:**")
        st.markdown("1. Make sure it's a valid PDF file")
        st.markdown("2. Try re-saving the PDF")
        st.markdown("3. Export from Word/Google Docs as PDF")
        
        if st.button("Back to Verdict"):
            st.session_state.page = 'verdict'
            st.rerun()

# ===================================
# PAGE: RESUME VERDICT
# ===================================

elif st.session_state.page == 'resume_verdict':
    r = st.session_state.resume_verdict
    
    st.markdown("## Resume Analysis")
    
    # Strength
    strength_color = {
        'Weak': '#dc2626',
        'Average': '#ea580c',
        'Strong': '#16a34a'
    }.get(r['resume_strength'], '#666')
    
    st.markdown(f"""
    <div style='background: {strength_color}15; padding: 1.5rem; border-radius: 8px; border-left: 4px solid {strength_color};'>
        <h2 style='color: {strength_color}; margin: 0;'>{r['resume_strength']}</h2>
        <p style='margin: 0.5rem 0 0 0;'>Market Readiness: {r['market_readiness_score']}/100</p>
    </div>
    """, unsafe_allow_html=True)
    
    # First impression
    st.markdown("#### First 10-Second Impression")
    st.info(r['first_impression'])
    
    # Strengths
    if r['strengths']:
        st.markdown("#### ✅ What Works")
        for s in r['strengths']:
            st.markdown(f"• {s}")
    
    # Red flags
    if r['red_flags']:
        st.markdown("#### 🚩 Red Flags")
        for flag in r['red_flags']:
            st.markdown(f"• {flag}")
    
    # Quick fixes
    st.markdown("#### ⚡ Quick Fixes (Do This Week)")
    for i, fix in enumerate(r['quick_fixes'], 1):
        st.markdown(f"{i}. {fix}")
    
    st.markdown("---")
    
    if st.button("Done - Start Over"):
        st.session_state.page = 'landing'
        st.session_state.answers = {}
        st.session_state.verdict = None
        st.session_state.resume_verdict = None
        st.rerun()
