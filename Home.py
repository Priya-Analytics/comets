import streamlit as st
import pandas as pd
import random

# Force strict cinematic wide-viewport configuration
st.set_page_config(page_title="comets | Core Matrix Control", layout="wide", page_icon="☄️")

# ☄️ HIGH-END GRAPHICAL INTERFACE OVERLAY OVERRIDES (CYBERPUNK GLASSMORPHISM)
st.markdown("""
<style>
    /* 🌠 ADVANCED PURE CSS INFINITE SPACE STARDUST & FALLING COMETS ENGINE */
    .stApp {
        background-color: #03060f !important;
        background-image: 
            radial-gradient(1px 1px at 20px 30px, #ffffff, transparent),
            radial-gradient(1px 1px at 75px 140px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 140px 70px, #93c5fd, transparent),
            radial-gradient(2px 2px at 250px 290px, #ffffff, transparent),
            radial-gradient(1px 1px at 310px 420px, #93c5fd, transparent),
            radial-gradient(1.5px 1.5px at 450px 110px, #ffffff, transparent);
        background-size: 550px 550px;
        position: relative;
        overflow: hidden;
    }

    /* Trajectory Animation Mechanics for Falling Space Rocks */
    @keyframes comet-trajectory-burn {
        0% { transform: translateY(-120px) translateX(120px) rotate(-45deg); opacity: 0; }
        5% { opacity: 1; }
        70% { opacity: 1; }
        100% { transform: translateY(115vh) translateX(-115vw) rotate(-45deg); opacity: 0; }
    }

    /* Real Plasma Comet 1 (Neon Cyan) */
    .stApp::before {
        content: "";
        position: fixed;
        top: -10%; right: -10%;
        width: 4px; height: 160px;
        background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(56,189,248,0.9) 20%, rgba(30,58,138,0) 100%);
        filter: drop-shadow(0px 0px 8px #38bdf8);
        border-radius: 4px;
        animation: comet-trajectory-burn 6s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    /* Real Plasma Comet 2 (Crimson Flare) */
    .stApp::after {
        content: "";
        position: fixed;
        top: -20%; right: 30%;
        width: 3px; height: 110px;
        background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(244,63,94,0.8) 25%, rgba(159,18,57,0) 100%);
        filter: drop-shadow(0px 0px 10px #f43f5e);
        border-radius: 4px;
        animation: comet-trajectory-burn 11s linear infinite;
        animation-delay: 2.5s;
        pointer-events: none;
        z-index: 0;
    }
    
    html, body {
        background-color: #03060f !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ NARROW LEFT SIDEBAR FOOTPRINT WIDTH OVERRIDE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(4, 6, 12, 0.96) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* 🔒 CLEANED SECURITY GATEWAY CONTAINER (BLUE BORDER & GLOW REMOVED) */
    .auth-terminal-box {
        background: rgba(14, 20, 38, 0.85) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px;
        padding: 35px !important;
        max-width: 550px;
        margin: 8% auto !important;
        position: relative;
        z-index: 999;
    }
    
    .terminal-header {
        font-family: 'Courier New', monospace;
        color: #94a3b8;
        font-size: 13px;
        letter-spacing: 2px;
        margin-bottom: 20px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 8px;
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

# 🔒 HIGH-SECURITY SERVER DATABASE EMULATION LAYER (USERNAME + PASSWORD)
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

# Persistent server memory log array for usernames
if "registered_users" not in st.session_state:
    st.session_state["registered_users"] = ["System_Admin", "Logistics_Core"]

def secure_gate_protocol():
    # PHASE A: FIRST-TIME SERVER DATABASE INITIALIZATION
    if st.session_state["master_password"] is None or st.session_state["master_username"] is None:
        st.markdown('<div class="auth-terminal-box">', unsafe_allow_html=True)
        st.markdown('<div class="terminal-header">🛰️ SERVER SETUP: CONFIGURE ACCOUNT STORAGE</div>', unsafe_allow_html=True)
        
        setup_user = st.text_input("Create Your Unique Username:", key="reg_user_init")
        setup_pass = st.text_input("Create Your Private Password:", type="password", key="reg_pass_init")
        confirm_pass = st.text_input("Confirm Private Password:", type="password", key="reg_pass_conf")
        
        if st.button("🔐 Register to Server Database", use_container_width=True):
            if setup_user.strip() == "":
                st.error("Username cannot be blank!")
            elif setup_pass == confirm_pass and setup_pass != "":
                clean_user = setup_user.strip()
                st.session_state["master_username"] = clean_user
                st.session_state["master_password"] = setup_pass
                st.session_state["authenticated"] = True
                
                if clean_user not in st.session_state["registered_users"]:
                    st.session_state["registered_users"].append(clean_user)
                    
                st.success("Account registered securely. Launching...")
                st.rerun()
            else:
                st.error("HANDSHAKE FAILS: Password fields do not match.")
        st.markdown('</div>', unsafe_allow_html=True)
        return False
        
    # PHASE B: AUTHORIZED USER SESSION ALREADY ACTIVE
    if st.session_state["authenticated"]:
        return True
        
    # PHASE C: THE QUANTUM TERMINAL INTERFACE LOGIN FORM
    st.markdown('<div class="auth-terminal-box">', unsafe_allow_html=True)
    st.markdown('<div class="terminal-header">🔒 ACCESS SHIELD: ACCOUNT VERIFICATION MANDATORY</div>', unsafe_allow_html=True)
    
    input_user = st.text_input("Enter Username:", key="login_user_node")
    input_pass = st.text_input("Enter Password:", type="password", key="login_pass_node")
    
    col_unlock, col_reset = st.columns(2)
    with col_unlock:
        if st.button("⚡ Verify Profile", use_container_width=True):
            if input_user == st.session_state["master_username"] and input_pass == st.session_state["master_password"]:
                st.session_state["authenticated"] = True
                
                if input_user not in st.session_state["registered_users"]:
                    st.session_state["registered_users"].append(input_user)
                    
                st.rerun()
            else:
                st.error("🛑 ACCESS DENIED: Invalid User or Password.")
    with col_reset:
        if st.button("❓ Reset Server Database", use_container_width=True):
            st.session_state["master_username"] = None
            st.session_state["master_password"] = None
            st.session_state["authenticated"] = False
            st.warning("Server account records wiped. Re-initializing setup...")
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
    return False

# 🚀 RUN LIVE PLATFORM DASHBOARD IF BOTH PARAMETERS MATCH
if secure_gate_protocol():
    # Narrow sidebar configuration
    st.sidebar.markdown("# ☄️ comets")
    st.sidebar.markdown(f"<p style='color:#38BDF8; font-size:11px;'>Active Session: <b>{st.session_state['master_username']}</b></p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader(label="", type=["csv", "xlsx"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Lock Portal / Exit", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

       # MAIN WORKSPACE HEADER VIEWPORTS
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
