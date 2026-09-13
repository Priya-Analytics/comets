import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import calendar
from datetime import datetime

st.set_page_config(page_title="Schedule & Streaks | comets", layout="wide")

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
    
    /* 🟩 UNIQUE GIT-STYLE MATRIX STREAKS GRADIENT LEVEL COLORS */
    .streak-grid-row {
        display: flex;
        gap: 5px;
        margin-top: 8px;
        flex-wrap: wrap;
    }
    .cell {
        width: 16px;
        height: 16px;
        border-radius: 3px;
        transition: transform 0.2s;
    }
    .cell:hover { transform: scale(1.2); }
    
    .lvl-0 { background-color: #161b22; border: 1px solid rgba(255,255,255,0.02); } /* No Use */
    .lvl-1 { background-color: #0e4429; } /* Light Use */
    .lvl-2 { background-color: #006d3a; } /* Medium Use */
    .lvl-3 { background-color: #26a641; } /* Heavy Use */
    .lvl-4 { background-color: #38bdf8; box-shadow: 0 0 8px #38bdf8; } /* Maximum Operations Use */
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
        // Stripped seconds configuration parameter array logic
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

# 📅 RENDER DYNAMIC FULL MONTH CALENDAR SQUARE MATRIX
st.subheader("🗓️ Calendar Matrix View")
now = datetime.now()
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
month_days = cal.monthdayscalendar(now.year, now.month)
day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Render Day Header Titles
cols = st.columns(7)
for idx, name in enumerate(day_names):
    cols[idx].markdown(f"<b style='color:#94A3B8;'>{name}</b>", unsafe_allow_html=True)

for week in month_days:
    cols = st.columns(7)
    for idx, day in enumerate(week):
        if day == 0:
            cols[idx].markdown("<div style='color:#334155; text-align:center;'>•</div>", unsafe_allow_html=True)
        elif day == now.day:
            cols[idx].markdown(f"<div style='background:#1E3A8A; border:1px solid #38BDF8; border-radius:6px; padding:10px; text-align:center; color:#FFF; font-weight:bold;'>{day}</div>", unsafe_allow_html=True)
        else:
            cols[idx].markdown(f"<div style='background:#111827; border:1px solid #1F2937; border-radius:6px; padding:10px; text-align:center; color:#E2E8F0;'>{day}</div>", unsafe_allow_html=True)

# 📝 ➕ NEW PLANNER OPTION CONNECTED DIRECTLY TO CALENDAR
st.markdown('<div class="widget-container">', unsafe_allow_html=True)
st.subheader("📝 Daily Operations Planner")

# Set up storage dictionary values inside the app runtime session scope memory
if "planner_notes" not in st.session_state:
    st.session_state["planner_notes"] = {}

p_day = st.number_input("Select Day to Plan:", min_value=1, max_value=31, value=int(now.day))
plan_key = f"day_{p_day}"

# Fetch existing data string values or fallback to empty context placeholder mapping
existing_note = st.session_state["planner_notes"].get(plan_key, "")
p_text = st.text_area(f"Input supply chain operations practice targets for Day {p_day}:", value=existing_note)

if st.button("💾 Log Targets to Calendar Memory"):
    st.session_state["planner_notes"][plan_key] = p_text
    st.success(f"Operational directives for Day {p_day} logged successfully!")
st.markdown('</div>', unsafe_allow_html=True)

# 🟩 UNIQUE GIT-STYLE MATRIX STREAKS AT BOTTOM PANEL (LIGHT TO DARK USAGE INTENSITY GRADIENT)
st.markdown('<div class="widget-container">', unsafe_allow_html=True)
st.markdown("### ☄️ Activity Streaks Matrix")
st.markdown("<p style='color:#94A3B8; font-size:13px;'>Usage density transitions from deep charcoal (idle) through dark green, bright green, and vibrant cyan based on daily script execution workloads.</p>", unsafe_allow_html=True)

# Display color code legend guide map parameters
st.markdown("""
<div style='display: flex; gap: 10px; align-items: center; margin-bottom: 15px; font-size: 11px; color: #94A3B8;'>
    <span>Less</span>
    <div class="cell lvl-0"></div>
    <div class="cell lvl-1"></div>
    <div class="cell lvl-2"></div>
    <div class="cell lvl-3"></div>
    <div class="cell lvl-4"></div>
    <span>More</span>
</div>
""", unsafe_allow_html=True)

# Generate a sequential activity timeline matrix row (Simulating 52 days of practice progress history)
st.markdown('<div class="streak-grid-row">', unsafe_allow_html=True)
simulated_usage_levels = [
    0,1,0,2,3,4,1,0,0,2,3,1,4,4,0,1,2,3,0,0,1,
    2,4,3,1,0,2,2,3,4,1,0,1,3,4,0,2,1,0,4,3,2,
    1,1,0,3,4,2,0,1,4,3
]

for level in simulated_usage_levels:
    st.markdown(f'<div class="cell lvl-{level}"></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
