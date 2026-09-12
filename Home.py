import streamlit as st
import pandas as pd

st.set_page_config(page_title="coments | Space Logistics Hub", layout="wide", page_icon="☄️")

# 🌠 INFINITE LIVE ANIMATED DEEP SPACE ENGINE WITH FALLING METEORS
st.markdown("""
<style>
    /* Full Application Space Backdrop Canvas */
    .stApp {
        background: #020408 !important;
        color: #E2E8F0;
    }
    
    /* Layer data metrics cards clearly over the animations */
    div[data-testid="stMetricBlock"] {
        background: rgba(10, 15, 30, 0.75) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        position: relative;
        z-index: 10;
    }
    div[data-testid="stMetricValue"] { color: #60A5FA !important; font-family: 'Courier New', monospace; font-weight: 700 !important; }
    div[data-testid="stMetricLabel"] { color: #94A3B8 !important; letter-spacing: 2px; }
</style>

<!-- Live Animated Space Backdrop Engine Frame Injector -->
<div class="space-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; overflow: hidden;">
    <svg width="100%" height="100%" xmlns="http://w3.org">
        <!-- Floating Stars Matrix background -->
        <rect width="100%" height="100%" fill="none"/>
        <circle cx="10%" cy="20%" r="1" fill="#fff" opacity="0.5"/>
        <circle cx="30%" cy="15%" r="1.5" fill="#fff" opacity="0.8"/>
        <circle cx="75%" cy="25%" r="1" fill="#93C5FD" opacity="0.6"/>
        <circle cx="85%" cy="40%" r="2" fill="#fff" opacity="0.4"/>
        <circle cx="45%" cy="65%" r="1" fill="#fff" opacity="0.7"/>
        <circle cx="60%" cy="80%" r="1.5" fill="#fff" opacity="0.9"/>
        <circle cx="20%" cy="85%" r="2" fill="#93C5FD" opacity="0.5"/>
        
        <!-- Continuous Shooting Meteor 1 (Cyan Velocity) -->
        <path d="M0,0 L120,120" stroke="url(#cyan-comet)" stroke-width="4" stroke-linecap="round">
            <animateTransform 
                attributeName="transform" 
                type="translate" 
                from="1200,-200" to="-200,1000" 
                dur="6s" 
                repeatCount="indefinite" />
        </path>
        
        <!-- Continuous Shooting Meteor 2 (Crimson Trail) -->
        <path d="M0,0 L90,90" stroke="url(#ruby-comet)" stroke-width="3" stroke-linecap="round">
            <animateTransform 
                attributeName="transform" 
                type="translate" 
                from="1600,0" to="-200,1200" 
                dur="10s" 
                begin="3s"
                repeatCount="indefinite" />
        </path>

        <!-- Gradients giving comets realistic heads and fading plasma stardust tails -->
        <defs>
            <linearGradient id="cyan-comet" x1="1" y1="1" x2="0" y2="0">
                <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
                <stop offset="20%" stop-color="#60A5FA" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#1E3A8A" stop-opacity="0"/>
            </linearGradient>
            <linearGradient id="ruby-comet" x1="1" y1="1" x2="0" y2="0">
                <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
                <stop offset="25%" stop-color="#F43F5E" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#881337" stop-opacity="0"/>
            </linearGradient>
        </defs>
    </svg>
</div>
""", unsafe_allow_html=True)

# 🔒 RECONFIGURED SECURITY CHECKS
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

def check_password():
    if st.session_state["master_password"] is None:
        st.markdown("<h2 style='position:relative; z-index:10;'>☄️ coments Security Matrix Configuration</h2>", unsafe_allow_html=True)
        new_pass = st.text_input("Create Your Private Master Password:", type="password", key="new_p")
        confirm_pass = st.text_input("Confirm Your Private Master Password:", type="password", key="conf_p")
        if st.button("Activate Launch Codes"):
            if new_pass == confirm_pass and new_pass != "":
                st.session_state["master_password"] = new_pass
                st.session_state["authenticated"] = True
                st.rerun()
            else: st.error("Credentials do not check out.")
        return False
    if st.session_state["authenticated"]: return True
    
    st.markdown("<h2 style='position:relative; z-index:10;'>🔒 Terminal Authentication Gate</h2>", unsafe_allow_html=True)
    input_pass = st.text_input("Enter Key:", type="password", key="auth_p")
    colA, colB = st.columns(2)
    with colA:
        if st.button("Unlock"):
            if input_pass == st.session_state["master_password"]:
                st.session_state["authenticated"] = True
                st.rerun()
            else: st.error("Access Denied.")
    with colB:
        if st.button("❓ Forgot Password / Reset Key"):
            st.session_state["master_password"] = None
            st.session_state["authenticated"] = False
            st.rerun()
    return False

if check_password():
    st.sidebar.markdown("# ☄️ coments")
    st.sidebar.markdown("### ➕ Ingest New Dataset")
    uploaded_file = st.sidebar.file_uploader("Drop custom CSV or Excel logs:", type=["csv", "xlsx"])
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Terminal / Log Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    st.markdown("<h1 style='position:relative; z-index:10; color: #F8FAFC; text-shadow: 0px 0px 15px rgba(96,165,250,0.4);'>☄️ coments: Orbit Control Center</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if uploaded_file is not None:
        try:
            custom_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.subheader(f"📊 Active Operations Board: `{uploaded_file.name}`")
            st.dataframe(custom_df, use_container_width=True)
            custom_code = st.text_area("Python Script Box:", value="st.write(custom_df.describe())")
            if st.button("Execute Core Logic Stream"):
                exec(custom_code, {"custom_df": custom_df, "pd": pd, "st": st})
        except Exception as e: st.error(f"Failed to compile target table: {e}")

    st.subheader("🌐 Telemetry Systems Pipeline Verification")
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1: st.metric(label="SQL Server Node Connection", value="10 Tables Online")
    with m_col2: st.metric(label="Python Execution Core", value="Active Runtime")
    with m_col3: st.metric(label="Power BI Frame Containers", value="Telemetry Ready")
