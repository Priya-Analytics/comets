import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Stars | comets", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

# 🎨 INJECT COMPACT CSS FOR CALENDAR AND BACKGROUND CLEANUP
st.markdown("""
<style>
    /* Downsize calendar box layout dimensions */
    div[data-testid="stDateInput"] {
        max-width: 160px !important;
    }
    div[data-testid="stDateInput"] > label {
        display: none !important; /* Forces total extraction of headers text fields */
    }
    /* Eliminate padding gaps to prevent blank ghost layout lines */
    .block-container {
        padding-top: 1.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

# 🛰️ REAL-TIME CHRONO-TELEMETRY ENGINE BLOCK (IST)
# Directly executes inside a zero-margin HTML block container layout string
st.components.v1.html("""
<div style="color: #E2E8F0; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif; font-size: 16px; line-height: 1.8;">
    <div style="margin-bottom: 6px;">⏰ <b>Time (IST):</b> <span id="ist-clock" style="color: #38BDF8; font-family: monospace; background: #0E1326; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.2);">--:--:--</span></div>
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
""", height=65)

# 📅 SMALL SIZE CALENDAR PICKER COMPONENT TOOL
st.date_input("", value=datetime.now(), key="clean_stars_calendar")
