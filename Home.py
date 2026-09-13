import streamlit as st
import pandas as pd
import random

# Force strict cinematic wide-viewport configuration
st.set_page_config(page_title="comets | Space Exploration", layout="wide", page_icon="🚀")

# 🌌 INJECT THEME DESIGN, REMOVE SIDEBAR COMPLETELY, AND SETUP NAV STYLES
st.markdown("""
<style>
    /* Google Fonts Calligraphy / Cursive font imports */
    @import url('https://googleapis.com');

    /* Gradient base matching the deep purple space atmosphere */
    .stApp {
        background: radial-gradient(circle at 70% 20%, #1c0a35 0%, #0d041a 50%, #05010c 100%) !important;
        background-attachment: fixed !important;
        color: #E2E8F0;
    }
    
    html, body {
        background-color: #05010c !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ REMOVE AND HIDE THE LEFT SIDEBAR PANEL ENTIRELY */
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
        width: 0px !important;
    }
    
    /* Adjust main content area to pull full width since sidebar is missing */
    [data-testid="stAppViewContainer"] {
        padding-left: 0px !important;
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
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.7);
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
        text-align: center;
        margin-top: 20px;
    }
    
    .sub-title-text {
        color: #94A3B8; 
        font-size: 16px; 
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* 📜 MOTIVATIONAL QUOTE CONTAINER */
    .quote-card-container {
        background: rgba(26, 15, 50, 0.55) !important;
        border: 1px solid rgba(255, 0, 127, 0.25) !important;
        backdrop-filter: blur(1px) !important;
        border-radius: 14px;
        padding: 35px;
        margin: 25px auto !important;
        max-width: 850px;
        box-shadow: 0 10px 32px 0 rgba(0, 0, 0, 0.4);
    }
    
    .calligraphy-text {
        font-family: 'Great Vibes', cursive, serif;
        font-size: 46px;
        color: #FFFFFF;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        line-height: 1.3;
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

# 🔒 SECURE SYSTEM MEMORY TRACKING HANDSHAKES
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False
if "show_login_form" not in st.session_state: st.session_state["show_login_form"] = False

# Function to run authentication login window prompts
def secure_gate_protocol():
    if st.session_state["authenticated"]:
        return True

    st.markdown("<h1 class='main-title'>🚀 comets: Space Exploring Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title-text'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)

    st.markdown("""
    <div class="quote-card-container">
        <p class="calligraphy-text">
            "A star wants to see himself rise to the top. <br/>
            A leader wants to see those around him rise to the top."
        </p>
        <span class="calligraphy-author">— Simon Sinek</span>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state["show_login_form"]:
        col_btn_l, col_btn_mid, col_btn_r = st.columns([0.35, 0.30, 0.35])
        with col_btn_mid:
            if st.button("🚀 Access Secure Terminal / Sign In", use_container_width=True):
                st.session_state["show_login_form"] = True
                st.rerun()
                
    if st.session_state["show_login_form"]:
        st.markdown('<div class="login-form-wrapper">', unsafe_allow_html=True)
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
                            st.switch_page("pages/11_Stars.py")
                        else: st.error("Passwords do not match.")
                with col_close1:
                    if st.form_submit_button("✖️ Close"):
                        st.session_state["show_login_form"] = False
                        st.rerun()
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
                            st.switch_page("pages/11_Stars.py")
                        else: st.error("Invalid user credentials.")
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

# 🚀 RUN PLATFORM HUB WORKSPACE ONCE FULLY AUTHORIZED
if secure_gate_protocol():
    # 🗺️ NEW REPLACED NAVIGATION INTERFACE BAR (MATCHING YOUR SKETCH DRAWING SHEET)
    nav_col1, nav_col2, nav_col3 = st.columns([0.2, 0.6, 0.2])
    
    with nav_col1:
        # Separate individual Home navigation trigger button
        home_clicked = st.button("🏠 Home", use_container_width=True)
        
    with nav_col2:
        # Dataset dropdown selector grouping all 10 analytics modules subpages together cleanly
        selected_module = st.selectbox(
            label="",
            options=[
                "Select Department Workspace Node...",
                "Demand Forecasting",
                "Inventory Optimization",
                "Carrier Performance",
                "Procurement Risk",
                "Last Mile",
                "Freight Audit",
                "Manufacturing",
                "Returns Logistics",
                "Cross Dock",
                "Omnichannel"
            ],
            label_visibility="collapsed"
        )
        
    with nav_col3:
        # Standalone button path shortcut linking to Stars
        stars_clicked = st.button("✨ Stars", use_container_width=True)

    # 🔀 REDIRECT MANIFEST ROUTING CONTROLLER RULES
    if stars_clicked:
        st.switch_page("pages/11_Stars.py")
        
    if selected_module != "Select Department Workspace Node...":
                # Dynamic path page redirection mapper engine (CONTINUED)
        page_mapping = {
            "Demand Forecasting": "pages/1_Demand_Forecasting.py",
            "Inventory Optimization": "pages/2_Inventory_Optimization.py",
            "Carrier Performance": "pages/3_Carrier_Performance.py",
            "Procurement Risk": "pages/4_Procurement_Risk.py",
            "Last Mile": "pages/5_Last_Mile.py",
            "Freight Audit": "pages/6_Freight_Audit.py",
            "Manufacturing": "pages/7_Manufacturing.py",
            "Returns Logistics": "pages/8_Returns_Logistics.py",
            "Cross Dock": "pages/9_Cross_Dock.py",
            "Omnichannel": "pages/10_Omnichannel.py"
        }
        st.switch_page(page_mapping[selected_module])

    st.markdown("---")

    # 🖥️ DISPLAY THE PRIMARY HOME CONTENT GRAPHICS LAYER
    st.markdown("<h1 class='main-title'>🚀 comets: Space Exploring Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title-text'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-card-container">
        <p class="calligraphy-text">
            "A star wants to see himself rise to the top. <br/>
            A leader wants to see those around him rise to the top."
        </p>
        <span class="calligraphy-author">— Simon Sinek</span>
    </div>
    """, unsafe_allow_html=True)

