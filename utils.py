"""
Career OS - Utility Functions
Helper functions for data processing and tracking
"""

import streamlit as st
from datetime import datetime

def get_client_ip():
    """Get user IP address (works in Streamlit Cloud)"""
    try:
        # Try to get from Streamlit's session info
        return st.context.headers.get("X-Forwarded-For", "unknown").split(',')[0]
    except:
        return "unknown"

def get_user_agent():
    """Get user agent string"""
    try:
        return st.context.headers.get("User-Agent", "unknown")
    except:
        return "unknown"

def calculate_session_duration(start_time):
    """Calculate how long user spent"""
    return (datetime.now() - start_time).total_seconds()

def format_currency(amount):
    """Format Indian currency"""
    if amount >= 10000000:  # 1 Cr+
        return f"₹{amount/10000000:.1f} Cr"
    elif amount >= 100000:  # 1 L+
        return f"₹{amount/100000:.1f} L"
    else:
        return f"₹{amount:,}"

def extract_pdf_text(file):
    """Extract text from PDF file"""
    try:
        import PyPDF2
        import io
        
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except:
        return None

def validate_answers(answers):
    """Validate all required questions answered"""
    required = ['career_stage', 'tech_stack', 'confidence', 'biggest_fear',
                'time_horizon', 'risk_appetite', 'priority', 'company_quality', 'skill_gap']
    
    for field in required:
        if field not in answers or not answers[field]:
            return False, f"Please answer: {field.replace('_', ' ')}"
    
    if len(answers.get('tech_stack', [])) == 0:
        return False, "Select at least one technology"
    
    return True, ""