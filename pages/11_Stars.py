import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Stars Practice Tracker | comets", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# ☄️ comets")
st.sidebar.info("Section: Personal Code Logger")

# 🎨 INJECT COMPACT GLOW COMPONENT OVERLAY STYLES
st.markdown("""
<style>
    /* Small Calendar Sizing Adjustments */
    div[data-testid="stDateInput"] {
        max-width: 160px !important;
    }
    div[data-testid="stDateInput"] > label {
        display: none !important; /* Remove Target Practice text label */
    }
    
    .quote-card {
        background: rgba(14, 20, 38, 0.7) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .widget-panel {
        background: rgba(14, 20, 38, 0.65) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .stat-val {
        font-family: 'Courier New', monospace;
        color: #38BDF8;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ Stars: Code Practice Terminal")
st.markdown("---")

# Layout Split: Left Chrono & Trackers Panel, Right Data Logger Canvas
left_widgets, right_logger = st.columns([0.35, 0.65], gap="large")

with left_widgets:
    # 🛰️ WIDGET BOX 1: REAL-TIME IST CHRONO TELEMETRY
    st.markdown('<div class="widget-panel">', unsafe_allow_html=True)
    st.markdown("### 🛰️ Chrono-Telemetry (IST)")
    
    # Live Clock & Date via custom JavaScript execution layer
    st.components.v1.html("""
    <div style="color: #E2E8F0; font-family: system-ui, sans-serif; font-size: 15px; line-height: 1.8;">
        <div>⏰ <b>Station Time:</b> <span id="ist-clock" style="color: #38BDF8; font-family: monospace; background: #090D1A; padding: 2px 6px; border-radius: 4px;">--:--:--</span></div>
        <div style="margin-top: 8px;">📅 <b>Current Date:</b> <span id="ist-date" style="color: #10B981;">--------</span></div>
    </div>
    <script>
        function updateIST() {
            const now = new Date();
            // Convert to Indian Standard Time (Asia/Kolkata) string format parameters
            const timeOptions = { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
            const dateOptions = { timeZone: 'Asia/Kolkata', weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            
            document.getElementById('ist-clock').textContent = now.toLocaleTimeString('en-US', timeOptions);
            document.getElementById('ist-date').textContent = now.toLocaleDateString('en-US', dateOptions);
        }
        setInterval(updateIST, 1000);
        updateIST();
    </script>
    """, height=65)
    
    # Downsized compact calendar select module layout
    selected_date = st.date_input("", value=datetime.now(), key="stars_calendar")
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔥 WIDGET BOX 2: DAILY & MONTHLY STREAK COUNTERS
    st.markdown('<div class="widget-panel">', unsafe_allow_html=True)
    st.markdown("### 🔥 Practice Streaks")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.markdown("⚡ **Daily Streak**")
        st.markdown('<div class="stat-val">5 Days</div>', unsafe_allow_html=True)
    with s_col2:
        st.markdown("🌙 **Monthly Streak**")
        st.markdown('<div class="stat-val">18 Days</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 📋 WIDGET BOX 3: RE-LOCATED TO-DO LIST TASK TRACKER
    st.markdown('<div class="widget-panel">', unsafe_allow_html=True)
    st.markdown("### 📋 Practice Checklist")
    t1 = st.checkbox("💻 Log Today's SQL Query Snippet", key="star_t1")
    t2 = st.checkbox("🐍 Log Today's Python Function", key="star_t2")
    t3 = st.checkbox("📄 Add Documentation Notes", key="star_t3")
    
    done = sum([t1, t2, t3])
    st.progress(done / 3.0)
    st.markdown(f"<p style='font-size:12px; color:#38BDF8; font-family:monospace; margin-top:5px;'>Sync Level: {done}/3 Completed</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right_logger:
    st.subheader("✍️ Log Daily Practice Snippets")
    
    if "saved_quotes" not in st.session_state:
        st.session_state["saved_quotes"] = [
            {"type": "SQL", "text": "SELECT SKU_ID, SUM(Historical_Orders) FROM Demand_History GROUP BY SKU_ID;", "date": "2026-09-13"},
            {"type": "Python", "text": "df['Stock_Value'] = df['Current_Stock_Level'] * df['Unit_Cost_USD']", "date": "2026-09-13"}
        ]
    
    q_type = st.selectbox("Select Language Type:", ["SQL", "Python", "Documentation Notes"])
    q_text = st.text_area("Paste code snippet or logic concept here:")
    
    if st.button("🚀 Upload to Stars Memory"):
        if q_text.strip() != "":
            new_entry = {
                "type": q_type,
                "text": q_text,
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            st.session_state["saved_quotes"].insert(0, new_entry)
            st.success("Snippet synchronized successfully!")
            st.rerun()
        else:
            st.error("Text field cannot be empty.")

    st.markdown("---")
    st.subheader("📜 Historical Practice Vault")
    
    for item in st.session_state["saved_quotes"]:
        badge_color = "#38BDF8" if item["type"] == "SQL" else "#A855F7" if item["type"] == "Python" else "#F43F5E"
        st.markdown(f"""
        <div class="quote-card">
            <span style="background:{badge_color}; color:white; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:bold;">{item["type"]}</span>
            <span style="color:#8B949E; font-size:12px; float:right;">📅 {item["date"]}</span>
            <pre style="margin-top:10px; color:#F8FAFC; background:#090D1A; padding:10px; border-radius:6px; font-family:monospace;">{item["text"]}</pre>
        </div>
        """, unsafe_allow_html=True)
