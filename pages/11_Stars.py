import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import calendar
from datetime import datetime

st.set_page_config(page_title="Schedule & SCM Telemetry | comets", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

# 🌌 LIVE JAVASCRIPT SPACE CANVAS BACKGROUND (STARS INBACKGROUND GENERATOR)
st.components.v1.html("""
<canvas id="starsSubCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #020306; z-index: -999; pointer-events: none;"></canvas>
<script>
    const canvas = document.getElementById('starsSubCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const stars = [];
    for(let i = 0; i < 250; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 1.5,
            opacity: Math.random()
        });
    }

    function draw() {
        ctx.fillStyle = '#020306';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let star of stars) {
            ctx.fillStyle = `rgba(255, 255, 255, ${star.opacity})`;
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();
            star.opacity += (Math.random() - 0.5) * 0.03;
            if(star.opacity < 0.1) star.opacity = 0.1;
            if(star.opacity > 1) star.opacity = 1;
        }
        requestAnimationFrame(draw);
    }
    draw();
</script>
""", height=0, scrolling=False)

# 🎨 INJECT COMPACT GLOW COMPONENT OVERLAY STYLES
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    html, body { background-color: #020306 !important; }

    iframe {
        width: 100% !important;
        height: 80px !important;
        border: none !important;
    }
    
    .schedule-header {
        color: #38BDF8 !important;
        font-family: 'Courier New', monospace;
        font-weight: 800;
        letter-spacing: 2px;
        font-size: 28px;
        margin-bottom: 15px;
    }

    .widget-container {
        background: rgba(14, 20, 38, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
    }
    
    /* 🟩 SCM SCENARIO BLOCK TELEMETRY CELLS COLORS */
    .scm-row {
        display: flex;
        gap: 6px;
        margin-top: 6px;
    }
    .scm-cell {
        width: 22px;
        height: 22px;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 10px;
        font-weight: bold;
        color: rgba(255,255,255,0.7);
    }
    .s-none { background-color: #161b22; }
    .s-sql { background-color: #0e4429; color: #38BDF8; }
    .s-py { background-color: #006d3a; color: #A855F7; }
    .s-bi { background-color: #26a641; color: #F59E0B; }
    .s-ops { background-color: #38bdf8; color: #020306; box-shadow: 0 0 6px #38bdf8; }
</style>
""", unsafe_allow_html=True)

# 📋 LEFT TITLE HEADER
st.markdown('<div class="schedule-header">📅 Schedule</div>', unsafe_allow_html=True)

# 🛰️ DYNAMIC REAL-TIME IST TELEMETRY ENGINE (HOURS & MINUTES ONLY - NO SECONDS)
st.components.v1.html("""
<div style="color: #E2E8F0; font-family: system-ui, sans-serif; font-size: 16px; line-height: 1.8; width: 100%;">
    <div style="margin-bottom: 6px;">⏰ <b>Time (IST):</b> <span id="ist-clock" style="color: #38BDF8; font-family: monospace; background: #0E1326; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.25);">--:--</span></div>
    <div>📅 <b>Date:</b> <span id="ist-date" style="color: #10B981; font-weight: 500;">--------</span></div>
</div>

<script>
    function runLiveIST() {
        const now = new Date();
        const timeParams = { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', hour12: true };
        const dateParams = { timeZone: 'Asia/Kolkata', weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        
        document.getElementById('ist-clock').textContent = now.toLocaleTimeString('en-US', timeParams);
        document.getElementById('ist-date').textContent = now.toLocaleDateString('en-US', dateParams);
    }
    setInterval(runLiveIST, 1000);
    runLiveIST();
</script>
""", height=80)

st.markdown("---")

# 📅 RENDER DYNAMIC FULL MONTH CALENDAR SQUARE MATRIX WITH BUILT-IN PLANNER NOTEBOOK
st.subheader("🗓️ Calendar Matrix & Planner Workspace")

# Initialize calendar notes memory store dictionary objects
if "planner_notes" not in st.session_state:
    st.session_state["planner_notes"] = {}

now = datetime.now()
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
month_days = cal.monthdayscalendar(now.year, now.month)
day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Main layout split into Calendar+Planner Grid on top, SCM telemetry on bottom
# Render Day Header Titles
c_headers = st.columns(7)
for idx, name in enumerate(day_names):
    c_headers[idx].markdown(f"<b style='color:#94A3B8; text-align:center; display:block;'>{name}</b>", unsafe_allow_html=True)

# Loop and render weeks
for week in month_days:
    c_days = st.columns(7)
    for idx, day in enumerate(week):
        if day == 0:
            c_days[idx].markdown("<div style='color:#334155; text-align:center; padding:10px;'>•</div>", unsafe_allow_html=True)
        elif day == now.day:
            # Check if text note notes values exist in memory mapping strings
            note_indicator = "📝" if f"day_{day}" in st.session_state["planner_notes"] and st.session_state["planner_notes"][f"day_{day}"].strip() != "" else ""
            c_days[idx].markdown(f"<div style='background:#1E3A8A; border:1px solid #38BDF8; border-radius:6px; padding:10px; text-align:center; color:#FFF; font-weight:bold;'>{day} {note_indicator}</div>", unsafe_allow_html=True)
        else:
            note_indicator = "📝" if f"day_{day}" in st.session_state["planner_notes"] and st.session_state["planner_notes"][f"day_{day}"].strip() != "" else ""
            c_days[idx].markdown(f"<div style='background:#111827; border:1px solid #1F2937; border-radius:6px; padding:10px; text-align:center; color:#E2E8F0;'>{day} {note_indicator}</div>", unsafe_allow_html=True)

# 📝 INTEGRATED PLANNER CONTROLS (Tucked cleanly inside the Calendar View boundary space context)
p_day = st.selectbox("🎯 Click Target Calendar Day to Plan / View Notes:", [d for w in month_days for d in w if d != 0], index=int(now.day)-1)
plan_key = f"day_{p_day}"

existing_note = st.session_state["planner_notes"].get(plan_key, "")
p_text = st.text_input(label=f"Directives Log for Day {p_day}:", value=existing_note, placeholder="Type your daily practice targets here (e.g., Practiced Window Functions on Procurement page)...")

if st.button("💾 Save Planner Target"):
    st.session_state["planner_notes"][plan_key] = p_text
    st.success(f"DIRECTIVE: Operations log for Day {p_day} locked into calendar tracking nodes.")
    st.rerun()

st.markdown("---")

# 🌐 REPLACED STREAKS MATRIX WITH LOGISTICS DRILL TELEMETRY MATRIX
st.markdown('<div class="widget-container">', unsafe_allow_html=True)
st.markdown("### ☄️ Supply Chain Operations Analytics Telemetry")
st.markdown("<p style='color:#94A3B8; font-size:13px;'>Tracks completed drills categorized across structural core analyst domains instead of general green box grids.</p>", unsafe_allow_html=True)

# Legend matrix mapping parameters
st.markdown("""
<div style='display: flex; gap: 15px; align-items: center; margin-bottom: 15px; font-size: 11px; color: #94A3B8; flex-wrap: wrap;'>
    <div style='display:flex; align-items:center; gap:5px;'><div class="scm-cell s-none"></div> <span>Idle</span></div>
    <div style='display:flex; align-items:center; gap:5px;'><div class="scm-cell s-sql">S</div> <span>SQL Auditing</span></div>
    <div style='display:flex; align-items:center; gap:5px;'><div class="scm-cell s-py">P</div> <span>Python Scripts</span></div>
    <div style='display:flex; align-items:center; gap:5px;'><div class="scm-cell s-bi">B</div> <span>Power BI Dashboards</span></div>
    <div style='display:flex; align-items:center; gap:5px;'><div class="scm-cell s-ops">O</div> <span>Operations Report Done</span></div>
</div>
""", unsafe_allow_html=True)

# Generate 4 structural practice matrix tracking rows mapping out historical analyst review items
t_cols = st.columns(4)
domains = ["Demand Plan Nodes", "Warehouse Hub Nodes", "Freight Logistics Nodes", "Sourcing Nodes"]
simulated_matrix = [
    ["s-sql", "s-none", "s-py", "s-bi", "s-ops", "s-sql", "s-py", "s-bi", "s-none", "s-ops", "s-sql", "s-bi"],
    ["s-none", "s-sql", "s-bi", "s-none", "s-py", "s-ops", "s-none", "s-sql", "s-bi", "s-py", "s-ops", "s-sql"],
    ["s-bi", "s-py", "s-ops", "s-sql", "s-none", "s-bi", "s-py", "s-sql", "s-ops", "s-none", "s-py", "s-bi"],
    ["s-sql", "s-none", "s-none", "s-bi", "s-py", "s-ops", "s-sql", "s-none", "s-py", "s-bi", "s-ops", "s-none"]
]

for idx, dom_name in enumerate(domains):
    with t_cols[idx]:
        st.markdown(f"<span style='font-size:12px; color:#60A5FA; font-family:monospace;'>{dom_name}</span>", unsafe_allow_html=True)
        st.markdown('<div class="scm-row">', unsafe_allow_html=True)
        for cell_type in simulated_matrix[idx]:
            char_tag = cell_type.split('-')[1][0].upper() if cell_type != "s-none" else "•"

st.markdown(f'{char_tag}', unsafe_allow_html=True)
st.markdown('', unsafe_allow_html=True)
st.markdown('', unsafe_allow_html=True)
