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
   COLOR SYSTEM (Luxury Palette)
====================================== */
:root {
    --bg-primary: #f8f6f2;
    --bg-card: rgba(255,255,255,0.65);
    --text-primary: #111111;
    --text-secondary: #5a5a5a;
    --accent-gold: #b89b5e;
    --accent-gold-soft: rgba(184,155,94,0.15);
    --border-soft: rgba(0,0,0,0.08);
}

/* ======================================
   GLOBAL BACKGROUND
====================================== */
html, body {
    background: linear-gradient(135deg, #f8f6f2 0%, #f1eee9 100%);
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
    color: #111;
}

.hero h3 {
    font-size: 1.2rem;
    color: var(--text-secondary);
    max-width: 580px;
    margin: 1.5rem auto 2.5rem auto;
    line-height: 1.7;
}

/* Subtle gold underline accent */
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
   BUTTONS (Luxury CTA)
====================================== */
.stButton > button {
    background: #111;
    color: white;
    font-weight: 600;
    border-radius: 14px;
    padding: 1rem 2.5rem;
    border: none;
    letter-spacing: -0.01em;
    transition: all 0.25s ease;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.stButton > button:hover {
    background: #1c1c1c;
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
    backdrop-filter: blur(20px);
    border-radius: 22px;
    padding: 2.8rem;
    border: 1px solid var(--border-soft);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.05),
        0 5px 15px rgba(0,0,0,0.04);
    animation: fadeUp 0.6s ease-out;
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
   RADIO OPTIONS (Luxury Cards)
====================================== */
.stRadio > div {
    display: grid;
    gap: 0.9rem;
}

.stRadio > div > label {
    padding: 1.2rem 1.6rem;
    border-radius: 16px;
    border: 1px solid var(--border-soft);
    background: white;
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
    background: white !important;
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
    border: 3px solid white;
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
    background: #d4c4a8;
    border-radius: 6px;
}

/* ======================================
   SELECTION COLOR
====================================== */
::selection {
    background: var(--accent-gold);
    color: white;
}

</style>
"""
