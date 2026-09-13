import streamlit as st
import pandas as pd
import random

# Force strict wide-viewport layout configuration
st.set_page_config(page_title="comets | Space Exploration", layout="wide", page_icon="🚀")

# 🌌 INJECT VECTOR SPACE ACCENTS AND HIGH-CONTRAST COLORS MATCHING THE IMAGE
st.markdown("""
<style>
    /* Google Fonts Calligraphy / Cursive font imports */
    @import url('https://googleapis.com');

    /* Gradient base matching the deep purple space nebula atmosphere */
    .stApp {
        background: radial-gradient(circle at 70% 20%, #1c0a35 0%, #0d041a 50%, #05010c 100%) !important;
        background-attachment: fixed !important;
        color: #E2E8F0;
    }
    
    html, body {
        background-color: #05010c !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ NARROW LEFT SIDEBAR MATCHING VIBRANT PURPLE SPACE PALETTE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(13, 4, 26, 0.95) !important;
        border-right: 1px solid rgba(255, 0, 127, 0.2) !important;
    }
    
    /* 🔒 SECURE LOGIN CONTAINER */
    div[data-testid="stForm"] {
        background: rgba(13, 4, 26, 0.8) !important;
        border: 1px solid rgba(0, 212, 255, 0.25) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px;
        padding: 35px !important;
        max-width: 500px;
        margin: 8% auto !important;
        position: relative;
        z-index: 999;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(255, 0, 127, 0.15);
    }
    
    .stTextInput>div>div>input {
        background-color: rgba(5, 1, 12, 0.7) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }
    
    .main-title { 
        font-size: 46px; 
        font-weight: 900; 
        color: #FFFFFF; 
        font-family: 'Montserrat', sans-serif;
        text-shadow: 0 4px 15px rgba(0,0,0,0.5), 0 0 25px rgba(0, 212, 255, 0.3);
        letter-spacing: 1px;
        position: relative; 
        z-index: 10; 
    }
    
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(5, 1, 12, 0.5) !important;
        border: 1px dashed rgba(255, 0, 127, 0.3) !important;
        border-radius: 10px !important;
    }
    
    /* 📜 MOTIVATIONAL PORTFOLIO QUOTE CARDS STYLING */
    .quote-card-container {
        background: rgba(26, 15, 50, 0.6) !important;
        border: 1px solid rgba(0, 212, 255, 0.15) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    .sinek-quote {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        color: #F8FAFC;
        line-height: 1.5;
    }
    
    .sinek-author {
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        color: #00D4FF;
        letter-spacing: 2px;
        font-weight: bold;
        margin-top: 10px;
        text-transform: uppercase;
    }
    
    /* 🖊️ CALLIGRAPHY OVERRIDE STYLES MATCHING THE WRITING IMAGE */
    .calligraphy-text {
        font-family: 'Great Vibes', cursive, serif;
        font-size: 48px;
        color: #FFFFFF;
        text-shadow: 0 0 15px rgba(255, 0, 127, 0.6);
        line-height: 1.2;
        padding: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# 🔒 SECURE SERVER DATABASE MEMORY INITIALIZATION
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

def secure_gate_protocol():
    if st.session_state["master_password"] is None or st.session_state["master_username"] is None:
        with st.form("server_database_setup_form"):
            st.markdown("<p style='color:#00D4FF; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🚀 ROCKET ENGINE SETUP: INITIALIZE PORTAL PROFILE</p>", unsafe_allow_html=True)
            setup_user = st.text_input("Create Station Username:", key="init_user_input")
            setup_pass = st.text_input("Create Station Password:", type="password", key="init_pass_input")
            confirm_pass = st.text_input("Confirm Station Password:", type="password", key="init_conf_input")
            
            if st.form_submit_button("🚀 Launch & Register Account", use_container_width=True):
                if setup_user.strip() == "":
                    st.error("Username cannot be blank.")
                elif setup_pass == confirm_pass and setup_pass != "":
                    st.session_state["master_username"] = setup_user.strip()
                    st.session_state["master_password"] = setup_pass
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("Passwords do not match.")
        return False
        
    if st.session_state["authenticated"]:
        return True
        
    with st.form("security_access_gateway_form"):
        st.markdown("<p style='color:#00D4FF; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🔒 SECURE TERMINAL GATEWAY LOGIN</p>", unsafe_allow_html=True)
        input_user = st.text_input("Username:", key="login_user_input")
        input_pass = st.text_input("Password:", type="password", key="login_pass_input")
        
        col_submit, col_wipe = st.columns(2)
        with col_submit:
            if st.form_submit_button("⚡ Verify Profile Token", use_container_width=True):
                if input_user == st.session_state["master_username"] and input_pass == st.session_state["master_password"]:
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("Invalid user credentials.")
        with col_wipe:
            if st.form_submit_button("❓ Reset Account Records", use_container_width=True):
                st.session_state["master_username"] = None
                st.session_state["master_password"] = None
                st.session_state["authenticated"] = False
                st.rerun()
    return False

# 🚀 RUN LIVE PLATFORM DASHBOARD IF SYSTEM IS FULLY AUTHORIZED
if secure_gate_protocol():
    st.sidebar.markdown("# 🚀 comets")
    st.sidebar.markdown(f"<p style='color:#00D4FF; font-size:11px;'>Mission Pilot: <b>{st.session_state['master_username']}</b></p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader(label="", type=["csv", "xlsx"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Cockpit / Exit", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    # MAIN WORKSPACE HUB VIEWPORTS
    st.markdown("<h1 class='main-title'>🚀 comets: Space Exploring Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94A3B8; font-size:15px;'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)
    st.markdown("---")

    # 📜 INTEGRATED MOTIVATIONAL PANEL SECTIONS
    quote_col1, quote_col2 = st.columns(2, gap="large")
    
    with quote_col1:
        st.markdown("""
        <div class="quote-card-container">
            <p class="sinek-quote">
                "A star wants to see himself rise to the top. <br/>
                <span style='color: #94A3B8;'>A leader wants to see those around him rise to the top."</span>
            </p>
            <p class="sinek-author">— Simon Sinek</p>
        </div>
        """, unsafe_allow_html=True)
        
    with quote_col2:
        st.markdown("""
        <div class="quote-card-container" style="border-color: rgba(255, 0, 127, 0.25);">
            <p style="color: #94A3B8; font-family: 'Montserrat', sans-serif; font-size: 11px; letter-spacing: 1px; margin-bottom: 5px; text-transform: uppercase;">
                ✍️ Strategic Muscle Memory Log
            </p>
            <p class="calligraphy-text">
                Building up that Muscle Memory
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if uploaded_file is not None:
        try:
            custom_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.subheader(f"📊 Active Flight Scratchpad Data: `{uploaded_file.name}`")
            st.dataframe(custom_df, use_container_width=True)
            custom_code = st.text_area("Python Script Box:", value="st.write(custom_df.describe())")
            if st.button("Execute Flight Logic Stream"):
                exec(custom_code, {"custom_df": custom_df, "pd": pd, "st": st})
        except Exception as e: 
            st.error(f"Failed to process manual file upload segment: {e}")
