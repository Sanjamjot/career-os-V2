def get_custom_css():
    return """
<style>

/* ======================================
   LUXURY FONT STACK
====================================== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* ======================================
   THEME-AWARE LUXURY COLOR SYSTEM
====================================== */

/* Default (Light Mode inherits Streamlit vars) */
:root {
    --bg-primary: var(--background-color);
    --bg-card: var(--secondary-background-color);
    --text-primary: var(--text-color);
    --text-secondary: rgba(120,120,120,0.9);

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

/* ======================================
   GLOBAL BACKGROUND
====================================== */
html, body {
    background: var(--bg-primary);
    color: var(--text-primary);
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    max-width: 860px;
    padding: 3.5rem 1.5rem 4rem 1.5rem;
    margin: auto;
}

/* ======================================
   HERO SECTION
====================================== */
.hero {
    text-align: center;
    padding: 5rem 0 3rem 0;
    animation: fadeUp 0.7s ease-out;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    color: var(--text-primary);
}

.hero h3 {
    font-size: 1.2rem;
    color: var(--text-secondary);
    max-width: 580px;
    margin: 1.5rem auto 2.5rem auto;
    line-height: 1.7;
}

.hero h1::after {
    content: "";
    display: block;
    width: 60px;
    height: 3px;
    margin: 1.5rem auto 0 auto;
    background: var(--accent-gold);
    border-radius: 3px;
}

/* ======================================
   BUTTONS
====================================== */
.stButton > button {
    background: var(--text-primary);
    color: var(--bg-primary);
    font-weight: 600;
    border-radius: 14px;
    padding: 1rem 2.5rem;
    border: none;
    letter-spacing: -0.01em;
    transition: all 0.25s ease;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.18);
}

.stButton > button:active {
    transform: translateY(0);
}

/* ======================================
   GLASS CARD FORM
====================================== */
.stForm {
    background: var(--bg-card);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    padding: 2.8rem;
    border: 1px solid var(--border-soft);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.05),
        0 5px 15px rgba(0,0,0,0.04);
    animation: fadeUp 0.6s ease-out;
}

/* Dark Glass Enhancement */
[data-theme="dark"] .stForm {
    background: rgba(30,30,30,0.6);
}

/* ======================================
   FORM LABELS
====================================== */
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

/* ======================================
   RADIO OPTIONS
====================================== */
.stRadio > div {
    display: grid;
    gap: 0.9rem;
}

.stRadio > div > label {
    padding: 1.2rem 1.6rem;
    border-radius: 16px;
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

/* ======================================
   INPUT FIELDS
====================================== */
.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input {
    border-radius: 14px !important;
    border: 1px solid var(--border-soft) !important;
    padding: 0.9rem !important;
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    transition: all 0.2s ease !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--accent-gold) !important;
    box-shadow: 0 0 0 3px var(--accent-gold-soft) !important;
}

/* ======================================
   SLIDER
====================================== */
.stSlider > div > div > div > div {
    background: var(--accent-gold);
    height: 6px;
}

.stSlider > div > div > div > div > div {
    background: var(--accent-gold);
    width: 22px;
    height: 22px;
    border: 3px solid var(--bg-primary);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* ======================================
   PROGRESS BAR
====================================== */
.stProgress > div > div {
    background: var(--accent-gold);
    border-radius: 10px;
}

/* ======================================
   ANIMATION
====================================== */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ======================================
   SCROLLBAR
====================================== */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: var(--accent-gold);
    border-radius: 6px;
}

/* ======================================
   SELECTION
====================================== */
::selection {
    background: var(--accent-gold);
    color: white;
}

</style>
"""
