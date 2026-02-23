def get_custom_css():
    return """
<style>

/* ================================
   PREMIUM COLOR SYSTEM (NO GOLD)
================================ */

/* Light Mode */
:root {
    --bg-main: #F5F6F8;
    --bg-card: #FFFFFF;
    --text-main: #111827;
    --text-muted: #6B7280;

    --accent: #1E3A8A;
    --accent-hover: #1D4ED8;
    --accent-soft: rgba(30,58,138,0.1);

    --border: rgba(0,0,0,0.08);
}

/* Dark Mode */
[data-theme="dark"] {
    --bg-main: #0F172A;
    --bg-card: #1E293B;
    --text-main: #F8FAFC;
    --text-muted: #CBD5E1;

    --accent: #3B82F6;
    --accent-hover: #60A5FA;
    --accent-soft: rgba(59,130,246,0.15);

    --border: rgba(255,255,255,0.08);
}

/* ================================
   GLOBAL
================================ */

html, body {
    background: var(--bg-main);
    color: var(--text-main);
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    max-width: 880px;
    padding: 3rem 1.5rem 4rem 1.5rem;
    margin: auto;
}

/* ================================
   HERO
================================ */

.hero {
    text-align: center;
    padding: 4rem 0 3rem 0;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.04em;
}

.hero h3 {
    font-size: 1.15rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 1.5rem auto 2rem auto;
    line-height: 1.7;
}

/* Accent line */
.hero h1::after {
    content: "";
    display: block;
    width: 70px;
    height: 3px;
    margin: 1.5rem auto 0 auto;
    background: var(--accent);
    border-radius: 3px;
}

/* ================================
   PREMIUM BUTTONS
================================ */

.stButton > button {
    border-radius: 16px;
    padding: 1rem 2.5rem;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: all 0.25s ease;
}

/* Primary */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent), var(--accent-hover));
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.2);
}

/* Secondary */
.stButton > button:not([kind="primary"]) {
    background: transparent;
    color: var(--text-main);
    border: 1.5px solid var(--border);
}

.stButton > button:not([kind="primary"]):hover {
    border-color: var(--accent);
    color: var(--accent);
}

/* ================================
   FORM CARD
================================ */

.stForm {
    background: var(--bg-card);
    border-radius: 20px;
    padding: 2.5rem;
    border: 1px solid var(--border);
    box-shadow: 0 25px 60px rgba(0,0,0,0.05);
}

/* Dark card refinement */
[data-theme="dark"] .stForm {
    box-shadow: 0 25px 60px rgba(0,0,0,0.4);
}

/* ================================
   RADIO SELECTED
================================ */

.stRadio > div > label[data-checked="true"] {
    border-color: var(--accent);
    background: var(--accent-soft);
    font-weight: 600;
}

/* ================================
   INPUT FOCUS
================================ */

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-soft) !important;
}

/* ================================
   PROGRESS
================================ */

.stProgress > div > div {
    background: var(--accent);
    border-radius: 10px;
}

</style>
"""
