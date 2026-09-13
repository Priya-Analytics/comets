import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import calendar
from datetime import datetime

st.set_page_config(page_title="Schedule | comets", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

# 🌌 LIVE JAVASCRIPT SPACE CANVAS BACKGROUND (STARS IN BACKGROUND GENERATOR)
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
</style>
""", unsafe_allow_html=True)

# 📋 LEFT TITLE HEADER
st.markdown('<div class="schedule-header">静态 🧬 Schedule</div>', unsafe_allow_html=True)

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

# 📅 RENDER DYNAMIC FULL MONTH CALENDAR SQUARE MATRIX
st.subheader("🗓️ Calendar Matrix View")
now = datetime.now()
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
month_days = cal.monthdayscalendar(now.year, now.month)
day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Render Day Header Titles
c_headers = st.columns(7)
for idx, name in enumerate(day_names):
    c_headers[idx].markdown(f"<b style='color:#94A3B8; text-align:center; display:block;'>{name}</b>", unsafe_allow_html=True)

# Loop and render week calendar grids
for week in month_days:
    c_days = st.columns(7)
    for idx, day in enumerate(week):
        if day == 0:
            c_days[idx].markdown("<div style='color:#334155; text-align:center; padding:10px;'>•</div>", unsafe_allow_html=True)
        elif day == now.day:
            # Highlight current active date node
            c_days[idx].markdown(f"<div style='background:#1E3A8A; border:1px solid #38BDF8; border-radius:6px; padding:10px; text-align:center; color:#FFF; font-weight:bold;'>{day}</div>", unsafe_allow_html=True)
        else:
            c_days[idx].markdown(f"<div style='background:#111827; border:1px solid #1F2937; border-radius:6px; padding:10px; text-align:center; color:#E2E8F0;'>{day}</div>", unsafe_allow_html=True)
