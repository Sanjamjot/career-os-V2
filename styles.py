def get_custom_css():
    return """
<style>

/* ================================
   PREMIUM FONT
================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* ================================
   THEME SYSTEM
================================ */
:root {
    --bg-main: var(--background-color);
    --bg-card: var(--secondary-background-color);
    --text-main: var(--text-color);
    --text-muted: rgba(140,140,140,0.9);

    --gold: #c6a96b;
    --gold-soft: rgba(198,169,107,0.18);

    --border: rgba(0,0,0,0.08);
}

[data-theme="dark"] {
    --gold: #e2c48a;
    --gold-soft: rgba(226,196,138,0.18);
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

.hero h1::after {
    content: "";
    display: block;
    width: 70px;
    height: 3px;
    margin: 1.5rem auto 0 auto;
    background: var(--gold);
    border-radius: 3px;
}

/* ================================
   PREMIUM BUTTONS
================================ */

/* Base */
.stButton > button {
    border-radius: 18px;
    padding: 1rem 2.8rem;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: all 0.25s ease;
}

/* Primary (Gold Luxury) */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--gold), #e0c187);
    color: #111;
    box-shadow: 0 12px 30px rgba(198,169,107,0.35);
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 40px rgba(198,169,107,0.45);
}

.stButton > button[kind="primary"]:active {
    transform: translateY(0);
}

/* Secondary (Elegant Outline) */
.stButton > button:not([kind="primary"]) {
    background: transparent;
    color: var(--text-main);
    border: 1.5px solid var(--border);
}

.stButton > button:not([kind="primary"]):hover {
    border-color: var(--gold);
    color: var(--gold);
    transform: translateY(-2px);
}

/* ================================
   CARD / FORM
================================ */
.stForm {
    background: var(--bg-card);
    backdrop-filter: blur(16px);
    border-radius: 24px;
    padding: 2.5rem;
    border: 1px solid var(--border);
    box-shadow: 0 25px 60px rgba(0,0,0,0.05);
}

[data-theme="dark"] .stForm {
    background: rgba(30,30,30,0.6);
}

/* ================================
   FORM LABELS
================================ */
.stRadio > label,
.stSelectbox > label,
.stMultiSelect > label,
.stSlider > label,
.stNumberInput > label {
    font-weight: 600;
    font-size: 1.05rem;
    margin-bottom: 0.8rem;
    display: block;
}

/* ================================
   INPUTS
================================ */
.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input {
    border-radius: 14px !important;
    border: 1px solid var(--border) !important;
    padding: 0.9rem !important;
    background: var(--bg-card) !important;
    color: var(--text-main) !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px var(--gold-soft) !important;
}

/* ================================
   RADIO CARDS
================================ */
.stRadio > div {
    display: grid;
    gap: 0.9rem;
}

.stRadio > div > label {
    padding: 1.1rem 1.5rem;
    border-radius: 16px;
    border: 1px solid var(--border);
    background: var(--bg-card);
    transition: all 0.25s ease;
}

.stRadio > div > label:hover {
    border-color: var(--gold);
    background: var(--gold-soft);
    transform: translateY(-2px);
}

.stRadio > div > label[data-checked="true"] {
    border-color: var(--gold);
    background: var(--gold-soft);
    font-weight: 600;
}

/* ================================
   SLIDER
================================ */
.stSlider > div > div > div > div {
    background: var(--gold);
    height: 6px;
}

.stSlider > div > div > div > div > div {
    background: var(--gold);
    width: 22px;
    height: 22px;
    border: 3px solid var(--bg-main);
}

/* ================================
   PROGRESS
================================ */
.stProgress > div > div {
    background: var(--gold);
    border-radius: 10px;
}

/* ================================
   SCROLLBAR
================================ */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: var(--gold);
    border-radius: 6px;
}

/* ================================
   SELECTION
================================ */
::selection {
    background: var(--gold);
    color: white;
}

</style>
"""
