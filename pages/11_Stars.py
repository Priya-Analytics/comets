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

# CSS for glassy quote cards
st.markdown("""
<style>
    .quote-card {
        background: rgba(14, 20, 38, 0.7) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .widget-panel {
        background: rgba(14, 20, 38, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ Stars: Code Practice Terminal")
st.markdown("---")

# Layout Split: Chrono-Telemetry on the Left, Quote Uploaders on the Right
left_chrono, right_logger = st.columns([0.35, 0.65], gap="large")

with left_chrono:
    st.markdown('<div class="widget-panel">', unsafe_allow_html=True)
    st.subheader("🛰️ Chrono-Telemetry")
    
    time_str = datetime.now().strftime("%I:%M:%S %p")
    date_str = datetime.now().strftime("%A, %B %d, %Y")
    
    st.markdown(f"**⏰ Station Time:** `{time_str}`")
    st.markdown(f"**📅 Current Date:** `{date_str}`")
    
    selected_date = st.date_input("📅 Target Practice Calendar View:", value=datetime.now(), key="stars_calendar")
    st.markdown(f"<p style='font-size:11px; color:#8B949E;'>Log Entry Context: Year {selected_date.year}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right_logger:
    st.subheader("✍️ Log Daily SQL & Python Practice Snippets")
    
    # Initialize the local workspace database memory
    if "saved_quotes" not in st.session_state:
        st.session_state["saved_quotes"] = [
            {"type": "SQL", "text": "SELECT SKU_ID, SUM(Historical_Orders) FROM Demand_History GROUP BY SKU_ID;", "date": "2026-09-12"},
            {"type": "Python", "text": "df['Stock_Value'] = df['Current_Stock_Level'] * df['Unit_Cost_USD']", "date": "2026-09-12"}
        ]
    
    # Input forms
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
            st.success("Snippet synchronized into workspace log matrix!")
            st.rerun()
        else:
            st.error("Text field cannot be empty.")

    st.markdown("---")
    st.subheader("📜 Historical Practice Vault")
    
    # Loop out and render saved items
    for item in st.session_state["saved_quotes"]:
        badge_color = "#38BDF8" if item["type"] == "SQL" else "#A855F7" if item["type"] == "Python" else "#F43F5E"
        st.markdown(f"""
        <div class="quote-card">
            <span style="background:{badge_color}; color:white; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:bold;">{item["type"]}</span>
            <span style="color:#8B949E; font-size:12px; float:right;">📅 {item["date"]}</span>
            <pre style="margin-top:10px; color:#F8FAFC; background:#090D1A; padding:10px; border-radius:6px; font-family:monospace;">{item["text"]}</pre>
        </div>
        """, unsafe_allow_html=True)
