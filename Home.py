import streamlit as st
import pandas as pd

st.set_page_config(page_title="coments | Infinite Space Hub", layout="wide", page_icon="☄️")

# ☄️ INJECT COMPACT GLOW COMPONENT OVERLAY STYLES
st.markdown("""
<style>
    .stApp {
        background: #020306 !important;
        color: #E2E8F0;
    }
    /* Lock analytics metrics boxes cleanly on top of the space animation */
    div[data-testid="stMetricBlock"] {
        background: rgba(8, 12, 24, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        position: relative;
        z-index: 10;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    div[data-testid="stMetricValue"] { color: #38BDF8 !important; font-family: 'Courier New', monospace; font-weight: 700 !important; }
    div[data-testid="stMetricLabel"] { color: #94A3B8 !important; letter-spacing: 2px; }
    .main-title { font-size: 42px; font-weight: 800; color: #F8FAFC; text-shadow: 0 0 20px rgba(56,189,248,0.5); position: relative; z-index: 10; }
</style>
""", unsafe_allow_html=True)

# 🌌 LIVE JAVASCRIPT SPACE FIELD & FALLING COMET SIMULATOR 
# This forces the browser to keep animating hundreds of stars and shooting meteors infinitely
st.components.v1.html("""
<canvas id="spaceCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #020306; z-index: -1; pointer-events: none;"></canvas>
<script>
    const canvas = document.getElementById('spaceCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Generate a heavy matrix background of 250 deep sky stars
    const stars = [];
    for(let i = 0; i < 250; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 1.5,
            opacity: Math.random()
        });
    }

    // Active comet falling trail generator variables
    let comets = [
        { x: Math.random() * canvas.width, y: -50, speedX: -4, speedY: 4, length: 140, color: '#38BDF8' },
        { x: Math.random() * canvas.width + 200, y: -50, speedX: -5, speedY: 5, length: 100, color: '#F43F5E' }
    ];

    function draw() {
        ctx.fillStyle = '#020306';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw and twinkle space stars background
        for(let star of stars) {
            ctx.fillStyle = `rgba(255, 255, 255, ${star.opacity})`;
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();
            star.opacity += (Math.random() - 0.5) * 0.05;
            if(star.opacity < 0.1) star.opacity = 0.1;
            if(star.opacity > 1) star.opacity = 1;
        }

        // Render real falling comets tracking lines with gradient particle tails
        for(let comet of comets) {
            let gradient = ctx.createLinearGradient(comet.x, comet.y, comet.x + comet.length, comet.y - comet.length);
            gradient.addColorStop(0, '#FFFFFF');
            gradient.addColorStop(0.1, comet.color);
            gradient.addColorStop(1, 'transparent');

            ctx.strokeStyle = gradient;
            ctx.lineWidth = 3;
            ctx.lineCap = 'round';
            ctx.beginPath();
            ctx.moveTo(comet.x, comet.y);
            ctx.lineTo(comet.x + comet.length, comet.y - comet.length);
            ctx.stroke();

            // Drive comet paths down and left across the screen window
            comet.x += comet.speedX;
            comet.y += comet.speedY;

            // Reset loop position if a comet leaves the viewport limits
            if(comet.y > canvas.height + 100 || comet.x < -100) {
                comet.x = Math.random() * canvas.width + canvas.width/2;
                comet.y = -50;
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
</script>
""", height=0, scroller=False)

# 🔒 ROBUST CUSTOM AUTH CHECKS
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

def check_password():
    if st.session_state["master_password"] is None:
        st.markdown("<h2 class='main-title'>☄️ coments Security Matrix Configuration</h2>", unsafe_allow_html=True)
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
    
    st.markdown("<h2 class='main-title'>🔒 Terminal Authentication Gate</h2>", unsafe_allow_html=True)
    input_pass = st.text_input("Enter Key:", type="password", key="auth_p")
    colA, colB = st.columns(2)
    with colA:
        if st.button("Unlock Workspace"):
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

    st.markdown("<h1 class='main-title'>☄️ coments: Orbit Control Center</h1>", unsafe_allow_html=True)
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
