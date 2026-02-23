"""
Career OS - Configuration
Centralized config for the entire application
"""

# ===================================
# QUESTIONS CONFIGURATION
# ===================================

QUESTIONS = [
    {
        "id": "career_stage",
        "type": "radio",
        "label": "What's your current situation?",
        "options": ["Intern", "Full-time Engineer", "Between Jobs", "Final Year Student"],
        "help": "Be honest - this determines everything"
    },
    {
        "id": "comp_gap",
        "type": "comp_range",
        "label": "Compensation Reality Check",
        "current_label": "Current annual package (₹) if internship write stipend*12",
        "target_label": "What you think you deserve (₹)",
        "help": "We'll tell you if you're delusional or underpaid"
        
    },
    {
        "id": "tech_stack",
        "type": "multiselect",
        "label": "Tech stack you actually know (not just 'aware of')",
        "options": [
            "React/Next.js", "Vue/Angular", "Node.js/Express", "Python/Django/FastAPI",
            "Java/Spring", "Go", "Rust", "SQL/PostgreSQL", "MongoDB/NoSQL",
            "Redis/Caching", "AWS/Cloud", "Docker/K8s", "System Design", "DSA (Leetcode Medium+)"
        ],
        "help": "Only select what you can actually build production features with",
        "min_selections": 1
    },
    {
        "id": "confidence",
        "type": "slider",
        "label": "How good are you really? (Be honest, we'll verify from resume)",
        "min": 1,
        "max": 5,
        "labels": ["Beginner", "Learning", "Competent", "Strong", "Expert"],
        "help": "1 = Still Googling basics | 5 = Can mentor others"
    },
    {
        "id": "biggest_fear",
        "type": "select",
        "label": "What keeps you up at night?",
        "options": [
            "Getting left behind by peers",
            "Never breaking into top companies",
            "Stuck in service company hell",
            "Can't crack interviews despite experience",
            "Wrong tech stack = wasted years",
            "Underpaid and exploited",
            "Imposter syndrome destroying me"
        ],
        "help": "The truth - what actually scares you?"
    },
    {
        "id": "time_horizon",
        "type": "radio",
        "label": "When do you want to make a move?",
        "options": ["ASAP (Within 2 months)", "Soon (3-6 months)", "Eventually (6-12 months)", "Just exploring"],
        "help": "This affects our recommendations"
    },
    {
        "id": "risk_appetite",
        "type": "radio",
        "label": "Risk tolerance for career decisions",
        "options": ["Conservative (Security first)", "Balanced (Calculated risks)", "Aggressive (High risk, high reward)"],
        "help": "Be honest - would you join a funded startup over TCS?"
    },
    {
        "id": "priority",
        "type": "radio",
        "label": "Right now, what matters MORE to you?",
        "options": ["Learning & Growth", "Money (Max CTC)", "Stability & WLB", "Brand Name"],
        "help": "You can only pick ONE. What's the real priority?"
    },
    {
        "id": "company_quality",
        "type": "select",
        "label": "Current company type (or last job if unemployed)",
        "options": [
            "Service Company (TCS, Wipro, Infosys, Accenture, etc.)",
            "Startup (Funded, <500 people)",
            "Product Company (Established, profitable)",
            "FAANG / Top Tier",
            "Unemployed / Student"
        ],
        "help": "Where are you NOW?"
    },
    {
        "id": "skill_gap",
        "type": "select",
        "label": "Your biggest weakness right now (brutal honesty)",
        "options": [
            "DSA - can't solve Leetcode Medium consistently",
            "System Design - don't know how real systems work",
            "Communication - can't explain my work clearly",
            "Depth - know many things, master of none",
            "Projects - built nothing real, only tutorials",
            "Interview Skills - freeze up in pressure",
            "No weakness - I'm already strong"
        ],
        "help": "This determines your 90-day action plan"
    }
]

# ===================================
# SHEET HEADERS (Silent Tracking)
# ===================================

SHEET_HEADERS = [
    "timestamp",
    "session_id",
    "career_stage",
    "current_comp",
    "target_comp",
    "comp_gap_percent",
    "tech_stack",
    "tech_count",
    "confidence_level",
    "biggest_fear",
    "time_horizon",
    "risk_appetite",
    "priority",
    "company_quality",
    "skill_gap",
    "verdict",
    "verdict_confidence",
    "should_switch",
    "resume_uploaded",
    "resume_strength",
    "market_readiness",
    "ip_address",
    "user_agent",
    "session_duration_seconds"
]

# ===================================
# AI PROMPTS
# ===================================

CAREER_SYSTEM_PROMPT = """You are Career OS — a brutally honest AI career advisor.

YOUR MISSION: Give advice that builds LONG-TERM career leverage, even if it hurts short-term feelings.

RULES:
- Optimize for 5-year trajectory, not next paycheck
- Call out delusions (overconfidence, wrong priorities, bad timing)
- Be specific, not generic
- No motivational BS
- If they should WAIT, say it clearly and why
- If they're READY, give exact action steps

TONE: Direct, slightly harsh, but caring (like a tough mentor)

OUTPUT: Valid JSON only, no markdown, no extra text."""

RESUME_SYSTEM_PROMPT = """You are Career OS Resume Analyzer.

YOUR JOB: Assess resume competitiveness for Indian tech market (Bangalore, Hyderabad, Pune, NCR).

FOCUS ON:
- Are projects real or just tutorial clones?
- Is experience depth or just resume padding?
- Does tech stack match market demand?
- Can this person actually get interviews?

BE HARSH: Most resumes are mediocre. Call it out.

OUTPUT: Valid JSON only."""

# ===================================
# VERDICT THRESHOLDS
# ===================================

VERDICT_LOGIC = {
    "SWITCH_NOW": {
        "conditions": ["confidence >= 4", "experience >= 2", "comp_gap < 30%", "time_horizon != 'Just exploring'"],
        "message": "You're ready. Start applying."
    },
    "BUILD_THEN_SWITCH": {
        "conditions": ["confidence >= 3", "skill_gap identified", "time_horizon in ['Soon', 'Eventually']"],
        "message": "Not ready yet. Fix gaps first."
    },
    "WAIT": {
        "conditions": ["experience < 1", "confidence <= 2", "comp_gap > 50%"],
        "message": "You'll damage your career if you switch now."
    },
    "PIVOT_STACK": {
        "conditions": ["wrong_stack", "company_quality == 'Service'"],
        "message": "Your stack is dead-end. Pivot urgently."
    }
}

# ===================================
# DESIGN TOKENS
# ===================================

COLORS = {
    "primary": "#000000",
    "secondary": "#1a1a1a",
    "accent": "#FF6B35",
    "success": "#16a34a",
    "warning": "#ea580c",
    "danger": "#dc2626",
    "muted": "#666666",
    "bg": "#fafafa",
    "card_bg": "#ffffff"
}

FONTS = {
    "heading": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "body": "'Inter', system-ui, sans-serif",
    "mono": "'JetBrains Mono', monospace"
}
