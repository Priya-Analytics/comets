import streamlit as st
import pandas as pd

# Page setup with custom tracking metrics
st.set_page_config(page_title="coments | Space Logistics Hub", layout="wide", page_icon="☄️")

# 🌠 ADVANCED SPACE CSS WITH FALLING COMETS ANIMATION
st.markdown("""
<style>
    /* Deep space layout background container */
    .stApp {
        background: radial-gradient(circle at center, #0B0E14 0%, #030508 100%);
        color: #E2E8F0;
        overflow-x: hidden;
    }
    
    /* Falling Comets Animation Engine */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: transparent;
        z-index: 0;
        pointer-events: none;
        background-image: 
            radial-gradient(1px 1px at 20px 30px, #fff, transparent),
            radial-gradient(1.5px 1.5px at 40px 70px, #fff, transparent),
            radial-gradient(2px 2px at 90px 150px, #93C5FD, transparent),
            radial-gradient(1px 1px at 150px 240px, #fff, transparent);
        background-size: 200px 300px;
    }

    /* CSS Keyframe simulation for space rock streaks */
    @keyframes comet-streak {
        0% { transform: translateY(-100px) translateX(100px) rotate(-45deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(120vh) translateX(-120vw) rotate(-45deg); opacity: 0; }
    }

    /* Injecting animated layout backdrops */
    .block-container::after {
        content: "";
        position: fixed;
        top: -10%; right: -10%;
        width: 4px; height: 120px;
        background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(147,197,253,0.9) 50%, rgba(59,130,246,0) 100%);
        animation: comet-streak 8s linear infinite;
        z-index: 0;
        pointer-events: none;
    }

    /* Second offset meteor block */
    .block-container::before {
        content: "";
        position: fixed;
        top: -20%; right: 30%;
        width: 3px; height: 90px;
        background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(244,63,94,0.8) 50%, rgba(225,29,72,0) 100%);
        animation: comet-streak 14s linear infinite;
        animation-delay: 3s;
        z-index: 0;
        pointer-events: none;
    }

    /* Glassmorphic card styling grid metrics */
    div[data-testid="stMetricBlock"] {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    }

    div[data-testid="stMetricValue"] {
        color: #60A5FA !important;
        font-family: 'Courier New', monospace;
        font-weight: 700 !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        letter-spacing: 2px;
        font-size: 11px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🔒 MASTER RETENTION HANDSHAKE VARIABLES
if "master_password" not in st.session_state:
    st.session_state["master_password"] = None
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["master_password"] is None:
        st.subheader("☄️ coments Security Matrix Configuration")
        new_pass = st.text_input("Create Your Private Master Password:", type="password")
        confirm_pass = st.text_input("Confirm Your Private Master Password:", type="password")
        if st.button("Activate Launch Codes"):
            if new_pass == confirm_pass and new_pass != "":
                st.session_state["master_password"] = new_pass
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Credentials do not check out.")
        return False
    if st.session_state["authenticated"]:
        return True
    
    st.subheader("🔒 Terminal Authentication Gate")
    input_pass = st.text_input("Enter Key:", type="password")
    if st.button("Unlock"):
        if input_pass == st.session_state["master_password"]:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Access Denied.")
    return False

if check_password():
    # ➕ THE CUSTOM FILE UPLOADER ENGINE WITH INTERACTIVE ICON
    st.sidebar.markdown("# ☄️ coments")
    st.sidebar.markdown("<p style='color:#64748B;'>Space-Velocity Analytics Console</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("### ➕ Ingest New Dataset")
    uploaded_file = st.sidebar.file_uploader(
        "Drop a newly downloaded CSV or Excel file right here to run scratchpad analytics:",
        type=["csv", "xlsx"]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Terminal / Log Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    # PRIMARY VIEWPORT HUB DESIGN
    st.markdown("<h1 style='color: #F8FAFC; text-shadow: 0px 0px 15px rgba(96,165,250,0.4);'>☄️ coments: Orbit Control Center</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94A3B8; font-size:15px;'>Personal Supply Chain & Logistics Control Plane Sandbox Environment</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)

    # 📥 DATA INPUT RENDER GATEWAY
    if uploaded_file is not None:
        st.markdown("""
        <div style='background: rgba(16,185,129,0.1); border: 1px solid #10B981; padding: 15px; border-radius: 8px; margin-bottom: 20px;'>
            🟢 <b>Payload Hook Secured:</b> Custom file registered without data corruption.
        </div>
        """, unsafe_allow_html=True)
        
        try:
            if uploaded_file.name.endswith('.csv'):
                custom_df = pd.read_csv(uploaded_file)
            else:
                custom_df = pd.read_excel(uploaded_file)
                
            st.subheader(f"📊 Active Operations Board: `{uploaded_file.name}`")
            st.dataframe(custom_df, use_container_width=True)
            
            # Interactive programming canvas for manual uploads
            st.subheader("🐍 Scratchpad Python Query Box")
            custom_code = st.text_area("Write transformation scripts for your custom dataset file layer:", 
                                       value="# Inspect columns and matrix data statistics\nst.write(custom_df.describe())")
            if st.button("Execute Core Logic Stream"):
                exec(custom_code, {"custom_df": custom_df, "pd": pd, "st": st})
            st.markdown("<hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Failed to compile target table structures: {e}")

    # ENVIRONMENT METRICS GRAPH DATA PLATFORMS
    st.subheader("🌐 Telemetry Systems Pipeline Verification")
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="SQL Server Node Connection", value="10 Tables Online")
    with m_col2:
        st.metric(label="Python Execution Core", value="Symmetric Loop Active")
    with m_col3:
        st.metric(label="Power BI Frame Containers", value="Telemetry Ready")
        
    st.markdown("<hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
    st.markdown("""
    ### 🚀 Operations Briefing
    * Use the **`➕ Ingest New Dataset`** tool on your left panel to run script analytics routines against any custom downloaded log file.
    * Use the sidebar navigation menu directory to switch departments and tackle targeted supply chain simulation parameters.
    """)
