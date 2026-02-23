def get_custom_css():
    return """
<style>

/* ============================================================
   CAREER OS DESIGN SYSTEM v3
   Modern SaaS / AI Startup Grade UI
============================================================ */

/* ============================================================
   FONT SYSTEM
============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ============================================================
   COLOR TOKENS
============================================================ */

/* Light Mode */
:root {
    --bg-main: #F4F6F8;
    --bg-elevated: #FFFFFF;
    --bg-subtle: #F9FAFB;

    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-muted: #94A3B8;

    --accent: #2563EB;
    --accent-hover: #1D4ED8;
    --accent-soft: rgba(37,99,235,0.12);

    --success: #16A34A;
    --warning: #F59E0B;
    --danger: #DC2626;

    --border: rgba(15,23,42,0.08);
    --border-strong: rgba(15,23,42,0.15);

    --shadow-sm: 0 2px 6px rgba(0,0,0,0.04);
    --shadow-md: 0 8px 20px rgba(0,0,0,0.08);
    --shadow-lg: 0 20px 60px rgba(0,0,0,0.12);
}

/* Dark Mode */
[data-theme="dark"] {
    --bg-main: #0B1120;
    --bg-elevated: #111827;
    --bg-subtle: #1E293B;

    --text-primary: #F8FAFC;
    --text-secondary: #CBD5E1;
    --text-muted: #64748B;

    --accent: #3B82F6;
    --accent-hover: #60A5FA;
    --accent-soft: rgba(59,130,246,0.15);

    --success: #22C55E;
    --warning: #FBBF24;
    --danger: #F87171;

    --border: rgba(255,255,255,0.08);
    --border-strong: rgba(255,255,255,0.15);

    --shadow-sm: 0 2px 6px rgba(0,0,0,0.4);
    --shadow-md: 0 8px 20px rgba(0,0,0,0.5);
    --shadow-lg: 0 20px 60px rgba(0,0,0,0.6);
}

/* ============================================================
   GLOBAL RESET
============================================================ */

html, body {
    background: var(--bg-main);
    color: var(--text-primary);
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    max-width: 1000px;
    padding: 3rem 2rem 5rem 2rem;
    margin: auto;
}

/* ============================================================
   TYPOGRAPHY SCALE
============================================================ */

h1 { font-size: 3rem; font-weight: 800; letter-spacing: -0.04em; }
h2 { font-size: 2.2rem; font-weight: 700; }
h3 { font-size: 1.6rem; font-weight: 600; }
h4 { font-size: 1.25rem; font-weight: 600; }

p {
    font-size: 1rem;
    line-height: 1.7;
    color: var(--text-secondary);
}

/* ============================================================
   BUTTON SYSTEM
============================================================ */

.stButton > button {
    border-radius: 14px;
    padding: 0.9rem 2.5rem;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
}

/* Primary */
.stButton > button[kind="primary"] {
    background: var(--accent);
    color: white;
    box-shadow: var(--shadow-md);
}

.stButton > button[kind="primary"]:hover {
    background: var(--accent-hover);
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

/* Secondary */
.stButton > button:not([kind="primary"]) {
    background: var(--bg-elevated);
    color: var(--text-primary);
    border: 1px solid var(--border);
}

.stButton > button:not([kind="primary"]):hover {
    border-color: var(--accent);
    color: var(--accent);
}

/* Danger */
.button-danger {
    background: var(--danger) !important;
    color: white !important;
}

/* ============================================================
   CARD SYSTEM
============================================================ */

.card {
    background: var(--bg-elevated);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-md);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

/* ============================================================
   FORM CONTAINER
============================================================ */

.stForm {
    background: var(--bg-elevated);
    border-radius: 24px;
    padding: 2.5rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-md);
}

/* ============================================================
   INPUT SYSTEM
============================================================ */

.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input,
textarea {
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    background: var(--bg-elevated) !important;
    color: var(--text-primary) !important;
    padding: 0.8rem !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within,
.stNumberInput > div > div > input:focus,
textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-soft) !important;
}

/* ============================================================
   RADIO CARDS
============================================================ */

.stRadio > div {
    display: grid;
    gap: 1rem;
}

.stRadio > div > label {
    background: var(--bg-elevated);
    padding: 1rem 1.5rem;
    border-radius: 16px;
    border: 1px solid var(--border);
    transition: all 0.2s ease;
}

.stRadio > div > label:hover {
    border-color: var(--accent);
    background: var(--accent-soft);
}

.stRadio > div > label[data-checked="true"] {
    border-color: var(--accent);
    background: var(--accent-soft);
    font-weight: 600;
}

/* ============================================================
   BADGES
============================================================ */

.badge {
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge-success { background: rgba(22,163,74,0.1); color: var(--success); }
.badge-warning { background: rgba(245,158,11,0.1); color: var(--warning); }
.badge-danger { background: rgba(220,38,38,0.1); color: var(--danger); }

/* ============================================================
   METRIC CARDS
============================================================ */

.metric-card {
    background: var(--bg-elevated);
    border-radius: 20px;
    padding: 1.8rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-sm);
}

.metric-card h3 {
    font-size: 2rem;
    font-weight: 700;
}

/* ============================================================
   PROGRESS
============================================================ */

.stProgress > div > div {
    background: var(--accent);
    border-radius: 8px;
}

/* ============================================================
   TABLE STYLING
============================================================ */

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    padding: 0.9rem;
    border-bottom: 1px solid var(--border);
    text-align: left;
}

th {
    color: var(--text-secondary);
    font-weight: 600;
}

/* ============================================================
   STEPPER UI
============================================================ */

.stepper {
    display: flex;
    gap: 2rem;
    align-items: center;
}

.step {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: var(--bg-subtle);
    border: 2px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
}

.step.active {
    background: var(--accent);
    color: white;
    border-color: var(--accent);
}

/* ============================================================
   TABS
============================================================ */

.stTabs [role="tab"] {
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
}

.stTabs [aria-selected="true"] {
    background: var(--accent-soft);
    color: var(--accent);
}

/* ============================================================
   ANIMATIONS
============================================================ */

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-up {
    animation: fadeUp 0.5s ease-out;
}

/* ============================================================
   SCROLLBAR
============================================================ */

::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 8px;
}

/* ============================================================
   SELECTION
============================================================ */

::selection {
    background: var(--accent);
    color: white;
}

</style>
"""
