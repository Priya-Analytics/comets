import streamlit as st
import pandas as pd
import random

# Force strict cinematic wide-viewport layout configuration
st.set_page_config(page_title="comets | Matrix Horizon", layout="wide", page_icon="☄️")

# 🌌 INJECT THEME GRADIENTS & COLOR PALETTES MATCHING YOUR IMAGE (STREAKS & ANIMATIONS REMOVED)
st.markdown("""
<style>
    /* Full Application Horizon Gradient Canvas */
    .stApp {
        background: linear-gradient(135deg, #090B18 0%, #151433 35%, #2B1E4A 65%, #4C265B 100%) !important;
        background-attachment: fixed !important;
        color: #E6EBF5;
    }
    
    html, body {
        background-color: #090B18 !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ NARROW LEFT SIDEBAR CUSTOM PALETTE OVERRIDE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(9, 11, 24, 0.95) !important;
        border-right: 1px solid rgba(76, 38, 91, 0.4) !important;
    }
    
    /* 🔒 CINEMATIC ACCESS SECURITY GATEWAY TERMINAL BOX */
    div[data-testid="stForm"] {
        background: rgba(14, 15, 36, 0.75) !important;
        border: 1px solid rgba(147, 197, 253, 0.15) !important;
        backdrop-filter: blur(25px) !important;
        border-radius: 16px;
        padding: 35px !important;
        max-width: 500px;
        margin: 10% auto !important;
        position: relative;
        z-index: 999;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(76, 38, 91, 0.3);
    }
    
    /* Clean inputs styling matching the purple-dusk theme */
    .stTextInput>div>div>input {
        background-color: rgba(9, 11, 24, 0.6) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(76, 38, 91, 0.5) !important;
    }

    /* Live Session Identity Board panel */
    .user-registry-box {
        background: rgba(14, 15, 36, 0.6) !important;
        border: 1px solid rgba(129, 140, 248, 0.2) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 14px !important;
        padding: 22px !important;
        margin-top: 25px;
        position: relative;
        z-index: 10;
    }
    
    .main-title { 
        font-size: 44px; 
        font-weight: 800; 
        color: #FFFFFF; 
        text-shadow: 0 4px 12px rgba(0,0,0,0.4), 0 0 20px rgba(129, 140, 248, 0.3);
        position: relative; 
        z-index: 10; 
    }
    
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(9, 11, 24, 0.5) !important;
        border: 1px dashed rgba(129, 140, 248, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🔒 ACCOUNT SECURE ACCOUNT REGISTRY STORAGE MEMORY INITIALIZATION
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

# Session log tracker matrices array data
if "active_user_history" not in st.session_state:
    st.session_state["active_user_history"] = ["System_Administrator", "Logistics_Core_Node"]

def secure_gate_protocol():
    # PHASE A: FIRST TIME RECONCILIATION SETUP PHASE
    if st.session_state["master_password"] is None or st.session_state["master_username"] is None:
        with st.form("server_database_setup_form"):
            st.markdown("<p style='color:#818CF8; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🛰️ SERVER INITIALIZATION SETUP</p>", unsafe_allow_html=True)
            setup_user = st.text_input("Create Station Username:", key="init_user_input")
            setup_pass = st.text_input("Create Station Password:", type="password", key="init_pass_input")
            confirm_pass = st.text_input("Confirm Station Password:", type="password", key="init_conf_input")
            
            if st.form_submit_button("🔐 Register to Server Database", use_container_width=True):
                if setup_user.strip() == "":
                    st.error("Profile username validation fault: field cannot be blank.")
                elif setup_pass == confirm_pass and setup_pass != "":
                    clean_name = setup_user.strip()
                    st.session_state["master_username"] = clean_name
                    st.session_state["master_password"] = setup_pass
                    st.session_state["authenticated"] = True
                    
                    if clean_name not in st.session_state["active_user_history"]:
                        st.session_state["active_user_history"].append(clean_name)
                    st.rerun()
                else:
                    st.error("Verification exception: password configuration mismatch.")
        return False
        
    # PHASE B: USER ID HANDSHAKE SECURED SUCCESSFULLY
    if st.session_state["authenticated"]:
        return True
        
    # PHASE C: AUTHENTICATION LOCK SCREEN CONTROL PANEL
    with st.form("security_access_gateway_form"):
        st.markdown("<p style='color:#818CF8; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🔒 SECURE TERMINAL GATEWAY LOGIN</p>", unsafe_allow_html=True)
        input_user = st.text_input("Username:", key="login_user_input")
        input_pass = st.text_input("Password:", type="password", key="login_pass_input")
        
        col_submit, col_wipe = st.columns(2)
        with col_submit:
            if st.form_submit_button("⚡ Verify Profile Token", use_container_width=True):
                if input_user == st.session_state["master_username"] and input_pass == st.session_state["master_password"]:
                    st.session_state["authenticated"] = True
                    if input_user not in st.session_state["active_user_history"]:
                        st.session_state["active_user_history"].append(input_user)
                    st.rerun()
                else:
                    st.error("HANDSHAKE EXCEPTION: Invalid user credentials.")
        with col_wipe:
            if st.form_submit_button("❓ Reset Account Records", use_container_width=True):
                st.session_state["master_username"] = None
                st.session_state["master_password"] = None
                st.session_state["authenticated"] = False
                st.rerun()
    return False

# 🚀 RUN LIVE PLATFORM DASHBOARD IF SYSTEM IS FULLY AUTHORIZED
if secure_gate_protocol():
    # Sidebar navigation items
    st.sidebar.markdown("# ☄️ comets")
    st.sidebar.markdown(f"<p style='color:#818CF8; font-size:11px;'>Session Holder: <b>{st.session_state['master_username']}</b></p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader(label="", type=["csv", "xlsx"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Lock Portal / Exit", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    # MAIN WORKSPACE HUB VIEWPORTS
    st.markdown("<h1 class='main-title'>☄️ comets: Orbit Control Center</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94A3B8; font-size:15px;'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)
    st.markdown("---")

    if uploaded_file is not None:
        try:
            custom_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.markdown(f"### 📂 Active Scratchpad Data: `{uploaded_file.name}`")
            st.dataframe(custom_df, use_container_width=True)
            custom_code = st.text_area("Python Script Box:", value="st.write(custom_df.describe())")
            if st.button("Execute Upload Logic Stream"):
                exec(custom_code, {"custom_df": custom_df, "pd": pd, "st": st})
            st.markdown("---")
        except Exception as e: st.error(f"Failed to process manual file upload segment: {e}")

    # 💾 LIVE MONITOR TERMINAL PANEL: ACCESS AND SESSION RECORDS LOGS
    st.markdown('<div class="user-registry-box">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#818CF8; font-family:monospace; font-weight:bold; margin-bottom:5px;'>📊 IDENTITY DATABASE AUDIT METRICS</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94A3B8; font-size:12px; margin-bottom:15px;'>Reviewing current active sessions and previous log accounts validated through system core nodes.</p>", unsafe_allow_html=True)
    
    # Loop over user session memories and map icons cleanly onto screen
    for user_profile in st.session_state["active_user_history"]:
        if user_profile == st.session_state["master_username"]:
            st.markdown(f"👤 <b style='color:#FFFFFF;'>{user_profile}</b> <span style='color:#10B981; font-size:12px; font-family:monospace;'>[CURRENT ACTIVE NODE]</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"👤 <span style='color:#94A3B8;'>{user_profile}</span> <span style='color:#64748B; font-size:11px; font-family:monospace;'>[HISTORICAL LOG RECORDED]</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
