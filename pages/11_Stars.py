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

# 🎨 INJECT ADVANCED FULL-WIDTH GRID STYLES
st.markdown("""
<style>
    /* Expand the frame so nothing gets cut in half */
    iframe {
        width: 100% !important;
        height: 85px !important;
        border: none !important;
    }
    
    .schedule-header {
        color: #38BDF8 !important;
        font-family: 'Courier New', monospace;
        font-weight: 800;
        letter-spacing: 2px;
        font-size: 28px;
        margin-bottom: 20px;
    }

    /* GitHub-style matrix grid layout box styles */
    .streak-container {
        background: rgba(14, 20, 38, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px;
        padding: 20px;
        margin-top: 40px;
    }
    
    .streak-grid {
        display: grid;
        grid-template-columns: repeat(7, 18px);
        grid-gap: 4px;
        margin-top: 10px;
    }
    
    /* Unique star theme activity cells matching GitHub style values */
    .cell {
        width: 18px;
        height: 18px;
        border-radius: 3px;
        background-color: #161b22;
    }
    .cell.active-low { background-color: #0e4429; border: 1px solid rgba(56,189,248,0.2); }
    .cell.active-med { background-color: #006d3a; }
    .cell.active-high { background-color: #26a641; box-shadow: 0 0 6px #26a641; }
    .cell.active-max { background-color: #38bdf8; box-shadow: 0 0 8px #38bdf8; }
</style>
""", unsafe_allow_html=True)

# 📋 LEFT TITLE HEADER
st.markdown('<div class="schedule-header">📅 Schedule</div>', unsafe_allow_html=True)

# 🛰️ DYNAMIC REAL-TIME IST TELEMETRY ENGINE
st.components.v1.html("""
<div style="color: #E2E8F0; font-family: system-ui, sans-serif; font-size: 16px; line-height: 1.8; width: 100%;">
    <div style="margin-bottom: 6px;">⏰ <b>Time (IST):</b> <span id="ist-clock" style="color: #38BDF8; font-family: monospace; background: #0E1326; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.25);">--:--:--</span></div>
    <div>📅 <b>Date:</b> <span id="ist-date" style="color: #10B981; font-weight: 500;">--------</span></div>
</div>

<script>
    function runLiveIST() {
        const now = new Date();
        const timeParams = { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
        const dateParams = { timeZone: 'Asia/Kolkata', weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        
        document.getElementById('ist-clock').textContent = now.toLocaleTimeString('en-US', timeParams);
        document.getElementById('ist-date').textContent = now.toLocaleDateString('en-US', dateParams);
    }
    setInterval(runLiveIST, 1000);
    runLiveIST();
</script>
""", height=85)

st.markdown("---")

# 📅 RENDER DYNAMIC FULL MONTH CALENDAR SQUARE MATRIX
st.subheader("🗓️ Calendar Matrix View")
now = datetime.now()
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
month_days = cal.monthdayscalendar(now.year, now.month)
day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Build responsive dynamic square column alignments
cols = st.columns(7)
for idx, name in enumerate(day_names):
    cols[idx].markdown(f"<b style='color:#94A3B8;'>{name}</b>", unsafe_allow_html=True)

for week in month_days:
    cols = st.columns(7)
    for idx, day in enumerate(week):
        if day == 0:
            cols[idx].markdown("<div style='color:#334155;'>•</div>", unsafe_allow_html=True)
        elif day == now.day:
            # Highlight the current station active calendar date
            cols[idx].markdown(f"<div style='background:#1E3A8A; border:1px solid #38BDF8; border-radius:6px; padding:10px; text-align:center; color:#FFF; font-weight:bold;'>{day}</div>", unsafe_allow_html=True)
        else:
            cols[idx].markdown(f"<div style='background:#111827; border:1px solid #1F2937; border-radius:6px; padding:10px; text-align:center; color:#E2E8F0;'>{day}</div>", unsafe_allow_html=True)

# 🟩 UNIQUE GIT-STYLE MATRIX STREAKS AT BOTTOM PANEL
st.markdown('<div class="streak-container">', unsafe_allow_html=True)
st.markdown("### ☄️ Unique Activity Streaks Matrix")
st.markdown("<p style='color:#94A3B8; font-size:13px;'>Track daily practice frequencies mapped across operations modules nodes.</p>", unsafe_allow_html=True)

# Simulated matrix data arrays mapping analytics frequencies
s_cols = st.columns(6)
for i in range(6):
    with s_cols[i]:
        st.markdown(f"<span style='font-size:11px; color:#64748B;'>Week {i+1}</span>", unsafe_allow_html=True)
        st.markdown('<div class="streak-grid">', unsafe_allow_html=True)
        # Generate mixed activity color densities
        st.markdown('<div class="cell active-high"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell active-low"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell active-med"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell active-max"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell active-low"></div>', unsafe_allow_html=True)
        st.markdown('<div class="cell active-high"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
st.markdown('</div>', unsafe_allow_html=True)
