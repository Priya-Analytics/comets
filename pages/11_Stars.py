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

# 🌌 LIVE JAVASCRIPT SPACE CANVAS BACKGROUND
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

# 🎨 INJECT OPTIMIZED ROW COMPRESSION CSS
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
    
    /* 🛠️ FORCE TOTAL VERTICAL GAP REMOVAL BETWEEN ROWS */
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
        margin-top: 0px !important;
        padding-top: 0px !important;
    }
    
    div[data-testid="stHorizontalBlock"] {
        margin-bottom: 4px !important; /* Tiny micro-gap between rows */
        gap: 6px !important; /* Horizontal gap between day containers */
    }
    
    /* Popover configuration tweaks */
    div[data-testid="stPopover"] > button {
        width: 100% !important;
        background-color: #111827 !important;
        border: 1px solid #1F2937 !important;
        color: #E2E8F0 !important;
        padding: 12px 5px !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        text-align: center !important;
    }
    
    div.current-day-btn > div[data-testid="stPopover"] > button {
        background-color: #1E3A8A !important;
        border: 1px solid #38BDF8 !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 10px rgba(56,189,248,0.25);
    }
</style>
""", unsafe_allow_html=True)

# 📋 LEFT TITLE HEADER
st.markdown('<div class="schedule-header">📅 Schedule</div>', unsafe_allow_html=True)

# 🛰️ DYNAMIC REAL-TIME IST TELEMETRY ENGINE
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

# 📅 RENDER COMPRESSED CALENDAR MATRIX
st.subheader("🗓️ Calendar Matrix View")

if "calendar_events" not in st.session_state:
    st.session_state["calendar_events"] = {}

now = datetime.now()
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
month_days = cal.monthdayscalendar(now.year, now.month)
day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Day Headers
c_headers = st.columns(7)
for idx, name in enumerate(day_names):
    c_headers[idx].markdown(f"<b style='color:#94A3B8; text-align:center; display:block; margin-bottom: 10px;'>{name}</b>", unsafe_allow_html=True)

# Compact Row Loop Mapping Execution
for week in month_days:
    c_days = st.columns(7)
    for idx, day in enumerate(week):
        if day == 0:
            c_days[idx].markdown("<div style='color:#334155; text-align:center; padding:10px;'>•</div>", unsafe_allow_html=True)
        else:
            day_key = f"day_{day}"
            has_event = day_key in st.session_state["calendar_events"] and st.session_state["calendar_events"][day_key].strip() != ""
            display_label = f"{day} 🔵" if has_event else f"{day}"
            
            if day == now.day:
                st.markdown('<div class="current-day-btn">', unsafe_allow_html=True)
                with c_days[idx].popover(display_label, use_container_width=True):
                    st.markdown(f"#### 📝 Directives for Day {day} (Today)")
                    existing_text = st.session_state["calendar_events"].get(day_key, "")
                    updated_text = st.text_area("Log your events or notes:", value=existing_text, key=f"input_{day}")
                    if st.button("Save", key=f"save_{day}"):
                        st.session_state["calendar_events"][day_key] = updated_text
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                with c_days[idx].popover(display_label, use_container_width=True):
                    st.markdown(f"#### 📝 Directives for Day {day}")
                    existing_text = st.session_state["calendar_events"].get(day_key, "")
                    updated_text = st.text_area("Log your events or notes:", value=existing_text, key=f"input_{day}")
                    if st.button("Save", key=f"save_{day}"):
                        st.session_state["calendar_events"][day_key] = updated_text
                        st.rerun()
