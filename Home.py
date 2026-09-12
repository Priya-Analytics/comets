import streamlit as st
import pandas as pd

st.set_page_config(page_title="coments | Space Logistics Hub", layout="wide", page_icon="☄️")

# 🌌 COGNITIVE SPACE EMULATOR WITH REAL GLOWING COMET ANIMATION
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #0B0E14 0%, #030508 100%);
        color: #E2E8F0;
    }
    
    @keyframes comet-streak {
        0% { transform: translateY(-150px) translateX(150px) rotate(-45deg); opacity: 0; }
        10% { opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateY(120vh) translateX(-120vw) rotate(-45deg); opacity: 0; }
    }

    /* Upgraded Plasma Comet 1 (Neon Cyan) */
    .block-container::after {
        content: "";
        position: fixed;
        top: -10%; right: -10%;
        width: 6px; height: 180px;
        background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(96,165,250,0.9) 20%, rgba(30,58,138,0) 100%);
        filter: drop-shadow(0px 0px 10px #60A5FA) blur(1px);
        border-radius: 50% 50% 0 0;
        animation: comet-streak 7s linear infinite;
        z-index: 0;
        pointer-events: none;
    }

    /* Upgraded Plasma Comet 2 (Crimson Flare) */
    .block-container::before {
        content: "";
        position: fixed;
        top: -20%; right: 40%;
        width: 4px; height: 120px;
        background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(244,63,94,0.8) 25%, rgba(159,18,57,0) 100%);
        filter: drop-shadow(0px 0px 12px #F43F5E) blur(1px);
        border-radius: 50% 50% 0 0;
        animation: comet-streak 12s linear infinite;
        animation-delay: 3s;
        z-index: 0;
        pointer-events: none;
    }

    div[data-testid="stMetricBlock"] {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    div[data-testid="stMetricValue"] { color: #60A5FA !important; font-family: 'Courier New', monospace; font-weight: 700 !important; }
    div[data-testid="stMetricLabel"] { color: #94A3B8 !important; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

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
            else: st.error("Credentials do not check out.")
        return False
    if st.session_state["authenticated"]: return True
    
    st.subheader("🔒 Terminal Authentication Gate")
    input_pass = st.text_input("Enter Key:", type="password")
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

    st.markdown("<h1 style='color: #F8FAFC; text-shadow: 0px 0px 15px rgba(96,165,250,0.4);'>☄️ coments: Orbit Control Center</h1>", unsafe_allow_html=True)
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
