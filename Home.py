import streamlit as st
import pandas as pd
import random

# Force strict wide-viewport layout configuration
st.set_page_config(page_title="comets | Space Exploration", layout="wide", page_icon="🚀")

# 🌌 INJECT VECTOR SPACE ACCENTS AND HIGH-CONTRAST COLORS MATCHING THE IMAGE
st.markdown("""
<style>
    /* Google Fonts Calligraphy / Cursive font imports matching your sample writing */
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
    
    /* 🛠️ NARROW LEFT SIDEBAR PALETTE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(13, 4, 26, 0.95) !important;
        border-right: 1px solid rgba(255, 0, 127, 0.2) !important;
    }
    
    /* 🔒 SECURE LOGIN CONTAINER */
    div.login-form-wrapper > div[data-testid="stForm"] {
        background: rgba(13, 4, 26, 0.85) !important;
        border: 1px solid rgba(0, 212, 255, 0.25) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px;
        padding: 35px !important;
        max-width: 500px;
        margin: 20px auto !important;
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
        text-align: center;
        margin-top: 30px;
    }
    
    .sub-title-text {
        color: #94A3B8; 
        font-size: 16px; 
        text-align: center;
        margin-bottom: 25px;
    }
    
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(5, 1, 12, 0.5) !important;
        border: 1px dashed rgba(255, 0, 127, 0.3) !important;
        border-radius: 10px !important;
    }
    
    /* 📜 MOTIVATIONAL PORTFOLIO QUOTE CONTAINER */
    .quote-card-container {
        background: rgba(26, 15, 50, 0.55) !important;
        border: 1px solid rgba(255, 0, 127, 0.25) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 14px;
        padding: 35px;
        margin: 25px auto !important;
        max-width: 850px;
        box-shadow: 0 10px 32px 0 rgba(0, 0, 0, 0.4), 0 0 20px rgba(255, 0, 127, 0.1);
    }
    
    /* 🖊️ CALLIGRAPHY TYPOGRAPHY OVERRIDE RULES FOR SIMON SINEK'S QUOTE */
    .calligraphy-text {
        font-family: 'Great Vibes', cursive, serif;
        font-size: 46px;
        color: #FFFFFF;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        line-height: 1.3;
        padding: 5px 0;
        text-align: center;
    }
    
    .calligraphy-author {
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        color: #FF007F;
        letter-spacing: 3px;
        font-weight: bold;
        margin-top: 15px;
        text-transform: uppercase;
        display: block;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 🔒 SECURE SERVER DATABASE MEMORY INITIALIZATION
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False
if "show_login_form" not in st.session_state: st.session_state["show_login_form"] = False

# Function to run authentication mechanics
def secure_gate_protocol():
    if st.session_state["authenticated"]:
        return True

    # 🚀 HEADER WORDS BROUGHT DIRECTLY INTO THE SIGN IN PORTAL PAGE LAYOUT
    st.markdown("<h1 class='main-title'>🚀 comets: Space Exploring Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title-text'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)

    # 🖊️ SIMON SINEK'S CALLIGRAPHY QUOTE
    st.markdown("""
    <div class="quote-card-container">
        <p class="calligraphy-text">
            "A star wants to see himself rise to the top. <br/>
            A leader wants to see those around him rise to the top."
        </p>
        <span class="calligraphy-author">— Simon Sinek</span>
    </div>
    """, unsafe_allow_html=True)

    # 🚀 INTERACTIVE SIGN IN TRIGGER BUTTON (BELOW THE QUOTE)
    if not st.session_state["show_login_form"]:
        col_btn_l, col_btn_mid, col_btn_r = st.columns([0.35, 0.30, 0.35])
        with col_btn_mid:
            if st.button("🚀 Access Secure Terminal / Sign In", use_container_width=True):
                st.session_state["show_login_form"] = True
                st.rerun()
                
    # EXPAND INPUT MODULES ONLY IF SIGN IN BUTTON IS TRIGGERED
    if st.session_state["show_login_form"]:
        st.markdown('<div class="login-form-wrapper">', unsafe_allow_html=True)
        
        # FIRST-TIME ACCOUNT SECTOR SETUP
        if st.session_state["master_password"] is None or st.session_state["master_username"] is None:
            with st.form("server_database_setup_form"):
                st.markdown("<p style='color:#00D4FF; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🚀 ROCKET ENGINE SETUP: INITIALIZE PORTAL PROFILE</p>", unsafe_allow_html=True)
                setup_user = st.text_input("Create Station Username:", key="init_user_input")
                setup_pass = st.text_input("Create Station Password:", type="password", key="init_pass_input")
                confirm_pass = st.text_input("Confirm Station Password:", type="password", key="init_conf_input")
                
                col_sub1, col_close1 = st.columns([0.7, 0.3])
                with col_sub1:
                    if st.form_submit_button("🚀 Launch & Register Account", use_container_width=True):
                        if setup_user.strip() == "":
                            st.error("Username cannot be blank.")
                        elif setup_pass == confirm_pass and setup_pass != "":
                            st.session_state["master_username"] = setup_user.strip()
                            st.session_state["master_password"] = setup_pass
                            st.session_state["authenticated"] = True
                            
                            # REDIRECT PROTOCOL ACCELERATION: Switch directly to the Stars Subpage memory location hook
                            st.switch_page("pages/11_Stars.py")
                        else:
                            st.error("Passwords do not match.")
                with col_close1:
                    if st.form_submit_button("✖️ Close"):
                        st.session_state["show_login_form"] = False
                        st.rerun()
                        
        # STANDARD SECURITY PORTAL ACCESS CHALLENGE
        else:
            with st.form("security_access_gateway_form"):
                st.markdown("<p style='color:#00D4FF; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🔒 SECURE TERMINAL GATEWAY LOGIN</p>", unsafe_allow_html=True)
                input_user = st.text_input("Username:", key="login_user_input")
                input_pass = st.text_input("Password:", type="password", key="login_pass_input")
                
                col_submit, col_wipe, col_close2 = st.columns([0.4, 0.4, 0.2])
                with col_submit:
                    if st.form_submit_button("⚡ Verify Token", use_container_width=True):
                        if input_user == st.session_state["master_username"] and input_pass == st.session_state["master_password"]:
                            st.session_state["authenticated"] = True
                            
                            # REDIRECT PROTOCOL ACCELERATION: Open Stars page directly
                            st.switch_page("pages/11_Stars.py")
                        else:
                            st.error("Invalid user credentials.")
                with col_wipe:
                    if st.form_submit_button("❓ Reset Records", use_container_width=True):
                        st.session_state["master_username"] = None
                        st.session_state["master_password"] = None
                        st.session_state["authenticated"] = False
                        st.session_state["show_login_form"] = False
                        st.rerun()
                with col_close2:
                    if st.form_submit_button("✖️"):
                        st.session_state["show_login_form"] = False
                        st.rerun()
                        
        st.markdown('</div>', unsafe_allow_html=True)
    return False

# FALLBACK FOR SIDEBAR ACTION MANIFEST NAVIGATION SESSIONS (CONTINUED)
if secure_gate_protocol():
    st.sidebar.markdown("# 🚀 comets")
    st.sidebar.markdown(f"<p style='color:#00D4FF; font-size:11px;'>Mission Pilot: <b>{st.session_state['master_username']}</b></p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader(label="", type=["csv", "xlsx"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Cockpit / Exit", use_container_width=True):
        st.session_state["authenticated"] = False
        st.session_state["show_login_form"] = False
        st.rerun()

    # If the user manually navigates back to Home page after authentication, redirect them immediately to keep them on the Stars workspace
    st.switch_page("pages/11_Stars.py")

