import streamlit as st
import pandas as pd
import random

# Force strict cinematic wide-viewport configuration
st.set_page_config(page_title="comets | Core Matrix Control", layout="wide", page_icon="☄️")

# 🌌 INJECT REAL-TIME TWINKLING NIGHT SKY & CRESCENT MOON BACKGROUND
st.markdown("""
<style>
    /* Full Application Night Sky Base Layer CSS */
    .stApp {
        background: linear-gradient(to bottom, #050814 0%, #0c1326 70%, #17223b 100%) !important;
        position: relative;
        overflow: hidden;
    }

    /* 🌙 GLOWING CRESCENT MOON LAYER */
    .stApp::before {
        content: "";
        position: fixed;
        top: 50px;
        right: 80px;
        width: 65px;
        height: 65px;
        border-radius: 50%;
        box-shadow: 15px 12px 0px 0px #fef3c7;
        filter: drop-shadow(0px 0px 20px rgba(254, 243, 199, 0.35));
        pointer-events: none;
        z-index: 0;
    }

    /* 🌟 TWINKLING STARS ANIMATION MECHANICAL LOOPS */
    @keyframes star-twinkle-loop {
        0%, 100% { opacity: 0.2; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.1); }
    }

    .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        pointer-events: none;
        z-index: 0;
        background-image: 
            radial-gradient(1.5px 1.5px at 60px 90px, #ffffff, transparent),
            radial-gradient(2px 2px at 190px 250px, #ffffff, transparent),
            radial-gradient(1px 1px at 340px 110px, #93c5fd, transparent),
            radial-gradient(2.5px 2.5px at 480px 410px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 620px 170px, #93c5fd, transparent),
            radial-gradient(2px 2px at 800px 460px, #ffffff, transparent),
            radial-gradient(1px 1px at 950px 310px, #ffffff, transparent),
            radial-gradient(2.5px 2.5px at 1150px 150px, #93c5fd, transparent);
        background-size: 500px 500px;
        animation: star-twinkle-loop 5s ease-in-out infinite;
    }
    
    html, body {
        background-color: #050814 !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ FORCE LOGIN FORM TO DISPLAY CENTERED OVER THE STARS BACKGROUND */
    div[data-testid="stForm"] {
        background: rgba(14, 20, 38, 0.85) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px;
        padding: 30px !important;
        max-width: 500px;
        margin: 10% auto !important;
        position: relative;
        z-index: 999;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    
    /* 🛠️ NARROW LEFT SIDEBAR FOOTPRINT WIDTH OVERRIDE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(4, 6, 12, 0.96) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* Top-Secret Encrypted CEO container card */
    .ceo-terminal {
        background: rgba(14, 20, 38, 0.75) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px !important;
        padding: 25px !important;
        position: relative;
        z-index: 10;
        margin-top: 15px;
    }
    
    /* Live Users History Audit Board Panel */
    .user-registry-box {
        background: rgba(14, 20, 38, 0.7) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 14px !important;
        padding: 22px !important;
        margin-top: 25px;
        position: relative;
        z-index: 10;
    }
    
    .ceo-title {
        color: #38BDF8 !important;
        font-family: 'Courier New', monospace;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 16px;
        margin-bottom: 10px;
    }
    
    .quote-box {
        font-family: 'Georgia', serif;
        font-style: italic;
        color: #F8FAFC;
        font-size: 17px;
        line-height: 1.6;
        border-left: 3px solid #F43F5E;
        padding-left: 15px;
        margin: 15px 0;
    }
    
    .main-title { font-size: 44px; font-weight: 800; color: #F8FAFC; position: relative; z-index: 10; }
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px dashed rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🔒 ACCOUNT STORAGE INITIALIZATION DATA NODES
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

# Session tracking memory arrays for concurrent and previous users
if "active_user_history" not in st.session_state:
    st.session_state["active_user_history"] = ["System_Administrator", "Logistics_Core_Node"]

def secure_gate_protocol():
    # PHASE A: FIRST TIME RECONCILIATION SETUP PHASE
    if st.session_state["master_password"] is None or st.session_state["master_username"] is None:
        with st.form("server_database_setup_form"):
            st.markdown("<p style='color:#38BDF8; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🛰️ SERVER INITIALIZATION SETUP</p>", unsafe_allow_html=True)
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
        st.markdown("<p style='color:#38BDF8; font-family:monospace; font-size:13px; font-weight:bold; text-align:center;'>🔒 SECURE TERMINAL GATEWAY LOGIN</p>", unsafe_allow_html=True)
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
    st.sidebar.markdown(f"<p style='color:#38BDF8; font-size:11px;'>Session Holder: <b>{st.session_state['master_username']}</b></p>", unsafe_allow_html=True)
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

    # 🔒 TOP-SECRET: HIDDEN CEO QUOTES TERMINAL AREA
    st.markdown("""
    <div class="ceo-terminal">
        <div class="ceo-title">🔒 RESTRICTED DIRECTIVE: ENCRYPTED EXECUTIVE LOGS</div>
        <p style="color: #94A3B8; font-size: 13px; margin-bottom: 15px;">
            Intercepting internal quantum channels. Strategic directives for comets network nodes are buffered below.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    ceo_quotes = [
        '"In global logistics, a delay in transit isn\'t a resource shortage—it\'s an information asymmetry problem. Optimize visibility, and speed takes care of itself." — Chief Executive Officer',
        '"The comets network doesn\'t build traditional tracks; we build resilient, self-healing supply pipelines across complex dimensions." — Chief Logistics Officer',
        '"A master data analyst doesn\'t stare at lagging indices. They forecast structural bottlenecks before manufacturing nodes throw failure codes." — Chief Technology Director',
        '"Efficiency is born when lead time drop matrices sync perfectly with dynamic automated replenishment variables." — Executive Operations Board',
        '"True supply chain optimization isn\'t about cutting total route costs. It is about building flexibility to survive localized network collapses." — Chief Procurement Officer'
    ]
    
    if "current_quote" not in st.session_state:
        st.session_state["current_quote"] = random.choice(ceo_quotes)
        
    if st.button("🔌 Decrypt Next Command Directive"):
        st.session_state["current_quote"] = random.choice(ceo_quotes)
        st.rerun()
        
    st.markdown(f'<div class="quote-box">{st.session_state["current_quote"]}</div>', unsafe_allow_html=True)
    st.markdown("---")

    # 💾 LIVE MONITOR TERMINAL PANEL: ACCESS AND SESSION RECORDS LOGS
    st.markdown('<div class="user-registry-box">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#38BDF8; font-family:monospace; font-weight:bold; margin-bottom:5px;'>📊 IDENTITY DATABASE AUDIT METRICS</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94A3B8; font-size:12px; margin-bottom:15px;'>Reviewing current active sessions and previous log accounts validated through system core nodes.</p>", unsafe_allow_html=True)
    
    # Loop over user session memories and map icons cleanly onto screen
    for user_profile in st.session_state["active_user_history"]:
        if user_profile == st.session_state["master_username"]:
            st.markdown(f"👤 <b style='color:#FFFFFF;'>{user_profile}</b> <span style='color:#10B981; font-size:12px; font-family:monospace;'>[CURRENT ACTIVE NODE]</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"👤 <span style='color:#94A3B8;'>{user_profile}</span> <span style='color:#64748B; font-size:11px; font-family:monospace;'>[HISTORICAL LOG RECORDED]</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

