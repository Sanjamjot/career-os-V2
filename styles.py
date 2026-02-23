def get_custom_css():
    return """
<style>

/* =====================================================
   PREMIUM FONT
===================================================== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* =====================================================
   THEME-AWARE COLOR SYSTEM
===================================================== */
:root {
    --bg-primary: var(--background-color);
    --bg-card: var(--secondary-background-color);
    --text-primary: var(--text-color);
    --text-secondary: rgba(130,130,130,0.9);

    --accent-gold: #b89b5e;
    --accent-gold-soft: rgba(184,155,94,0.15);

    --border-soft: rgba(0,0,0,0.08);
}

/* Dark Mode Overrides */
[data-theme="dark"] {
    --accent-gold: #d4b97f;
    --accent-gold-soft: rgba(212,185,127,0.18);
    --border-soft: rgba(255,255,255,0.08);
}

/* =====================================================
   GLOBAL
===================================================== */
html, body {
    background: var(--bg-primary);
    color: var(--text-primary);
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    max-width: 900px;
    padding: 3rem 1.5rem 4rem 1.5rem;
    margin: auto;
}

/* =====================================================
   HERO SECTION
===================================================== */
.hero {
    text-align: center;
    padding: 4rem 0 3rem 0;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    color: var(--text-primary);
}

.hero h3 {
    font-size: 1.2rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 1.5rem auto 2rem auto;
    line-height: 1.7;
}

.hero h1::after {
    content: "";
    display: block;
    width: 70px;
    height: 3px;
    margin: 1.5rem auto 0 auto;
    background: var(--accent-gold);
    border-radius: 3px;
}

/* =====================================================
   PREMIUM BUTTON SYSTEM
===================================================== */
.stButton > button {
    border-radius: 16px;
    padding: 1rem 2.5rem;
    font-weight: 600;
    letter-spacing: -0.01em;
    border: none;
    cursor: pointer;
    transition: all 0.25s ease;
}

/* PRIMARY */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent-gold), #d4b97f);
    color: #111;
    box-shadow:
        0 10px 25px rgba(184,155,94,0.3),
        0 4px 10px rgba(0,0,0,0.12);
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px);
    box-shadow:
        0 15px 35px rgba(184,155,94,0.4),
        0 6px 18px rgba(0,0,0,0.15);
}

.stButton > button[kind="primary"]:active {
    transform: translateY(0);
}

/* SECONDARY */
.stButton > button:not([kind="primary"]) {
    background: transparent;
    color: var(--text-primary);
    border: 1.5px solid var(--border-soft);
}

.stButton > button:not([kind="primary"]):hover {
    border-color: var(--accent-gold);
    color: var(--accent-gold);
    transform: translateY(-2px);
}

/* =====================================================
   GLASS FORM CARD
===================================================== */
.stForm {
    background: var(--bg-card);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    padding: 2.5rem;
    border: 1px solid var(--border-soft);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.05),
        0 5px 15px rgba(0,0,0,0.04);
}

/* Dark Glass */
[data-theme="dark"] .stForm {
    background: rgba(30,30,30,0.6);
}

/* =====================================================
   FORM LABELS
===================================================== */
.stRadio > label,
.stSelectbox > label,
.stMultiSelect > label,
.stSlider > label,
.stNumberInput > label {
    font-weight: 600;
    font-size: 1.05rem;
    margin-bottom: 0.8rem;
    display: block;
    color: var(--text-primary);
}

/* =====================================================
   RADIO OPTIONS
===================================================== */
.stRadio > div {
    display: grid;
    gap: 0.9rem;
}

.stRadio > div > label {
    padding: 1.1rem 1.4rem;
    border-radius: 14px;
    border: 1px solid var(--border-soft);
    background: var(--bg-card);
    transition: all 0.3s ease;
    font-weight: 500;
}

.stRadio > div > label:hover {
    border-color: var(--accent-gold);
    background: var(--accent-gold-soft);
    transform: translateY(-2px);
}

.stRadio > div > label[data-checked="true"] {
    border-color: var(--accent-gold);
    background: var(--accent-gold-soft);
    font-weight: 600;
}

/* =====================================================
   INPUT FIELDS
===================================================== */
.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input {
    border-radius: 14px !important;
    border: 1px solid var(--border-soft) !important;
    padding: 0.9rem !important;
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--accent-gold) !important;
    box-shadow: 0 0 0 3px var(--accent-gold-soft) !important;
}

/* =====================================================
   SLIDER
===================================================== */
.stSlider > div > div > div > div {
    background: var(--accent-gold);
    height: 6px;
}

.stSlider > div > div > div > div > div {
    background: var(--accent-gold);
    width: 22px;
    height: 22px;
    border: 3px solid var(--bg-primary);
}

/* =====================================================
   PROGRESS BAR
===================================================== */
.stProgress > div > div {
    background: var(--accent-gold);
    border-radius: 10px;
}

/* =====================================================
   SCROLLBAR
===================================================== */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: var(--accent-gold);
    border-radius: 6px;
}

/* =====================================================
   TEXT SELECTION
===================================================== */
::selection {
    background: var(--accent-gold);
    color: white;
}

</style>
"""
