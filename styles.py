def get_custom_css():
    return """
<style>

/* ============================================================
   APPLE-STYLE DESIGN SYSTEM
============================================================ */

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* ============================================================
   COLOR SYSTEM (APPLE MINIMAL)
============================================================ */

/* Light */
:root {
    --bg-main: #ffffff;
    --bg-soft: #f5f5f7;
    --bg-glass: rgba(255,255,255,0.7);

    --text-primary: #1d1d1f;
    --text-secondary: #6e6e73;

    --accent: #0071e3;
    --accent-hover: #0058b0;

    --border: rgba(0,0,0,0.08);
}

/* Dark */
[data-theme="dark"] {
    --bg-main: #000000;
    --bg-soft: #111111;
    --bg-glass: rgba(28,28,30,0.6);

    --text-primary: #f5f5f7;
    --text-secondary: #86868b;

    --accent: #2997ff;
    --accent-hover: #409cff;

    --border: rgba(255,255,255,0.08);
}

/* ============================================================
   GLOBAL
============================================================ */

html, body {
    background: var(--bg-main);
    color: var(--text-primary);
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    max-width: 1100px;
    padding: 5rem 2rem;
    margin: auto;
}

/* ============================================================
   HERO SECTION (BIG APPLE STYLE)
============================================================ */

.hero {
    text-align: center;
    padding: 6rem 0 4rem 0;
    animation: fadeIn 0.8s ease-out;
}

.hero h1 {
    font-size: 4rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
}

.hero h3 {
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text-secondary);
    margin-top: 1.5rem;
    line-height: 1.6;
}

/* ============================================================
   GLASS CARD SECTIONS
============================================================ */

.stForm {
    background: var(--bg-glass);
    backdrop-filter: blur(30px);
    border-radius: 28px;
    padding: 3rem;
    border: 1px solid var(--border);
    box-shadow: 0 30px 80px rgba(0,0,0,0.06);
    animation: fadeInUp 0.6s ease-out;
}

/* ============================================================
   BUTTONS (APPLE FLOATING)
============================================================ */

.stButton > button {
    border-radius: 999px;
    padding: 0.9rem 2.8rem;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    transition: all 0.25s ease;
    cursor: pointer;
}

/* Primary */
.stButton > button[kind="primary"] {
    background: var(--accent);
    color: white;
}

.stButton > button[kind="primary"]:hover {
    background: var(--accent-hover);
    transform: scale(1.04);
}

/* Secondary */
.stButton > button:not([kind="primary"]) {
    background: var(--bg-soft);
    color: var(--text-primary);
    border: 1px solid var(--border);
}

.stButton > button:not([kind="primary"]):hover {
    transform: scale(1.04);
}

/* ============================================================
   INPUTS (CLEAN & ROUNDED)
============================================================ */

.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input {
    border-radius: 16px !important;
    border: 1px solid var(--border) !important;
    padding: 1rem !important;
    background: var(--bg-soft) !important;
    color: var(--text-primary) !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--accent) !important;
}

/* ============================================================
   RADIO (APPLE STYLE CARDS)
============================================================ */

.stRadio > div {
    display: grid;
    gap: 1rem;
}

.stRadio > div > label {
    padding: 1.2rem 1.5rem;
    border-radius: 20px;
    border: 1px solid var(--border);
    background: var(--bg-soft);
    transition: all 0.25s ease;
}

.stRadio > div > label:hover {
    transform: translateY(-3px);
}

.stRadio > div > label[data-checked="true"] {
    border-color: var(--accent);
    background: rgba(0,113,227,0.08);
    font-weight: 600;
}

/* ============================================================
   PROGRESS BAR
============================================================ */

.stProgress > div > div {
    background: var(--accent);
    border-radius: 20px;
}

/* ============================================================
   ANIMATIONS
============================================================ */

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* ============================================================
   SCROLLBAR (MINIMAL)
============================================================ */

::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: var(--text-secondary);
    border-radius: 8px;
}

::selection {
    background: var(--accent);
    color: white;
}

</style>
"""
