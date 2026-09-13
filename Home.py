import streamlit as st
import pandas as pd
import random

# Force strict cinematic wide-viewport configuration
st.set_page_config(page_title="comets | Core Matrix Control", layout="wide", page_icon="☄️")

# ☄️ HIGH-END GRAPHICAL INTERFACE OVERLAY OVERRIDES (CYBERPUNK GLASSMORPHISM)
st.markdown("""
<style>
    .stApp {
        background: transparent !important;
    }
    html, body {
        background-color: #020409 !important;
        overflow-x: hidden;
    }
    
    /* 🛠️ NARROW LEFT SIDEBAR FOOTPRINT WIDTH OVERRIDE */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(4, 6, 12, 0.96) !important;
        border-right: 1px solid rgba(56, 189, 248, 0.15) !important;
    }
    
    /* 🔒 CYBERPUNK ACCESS SECURITY GATEWAY CONTAINER */
    .auth-terminal-box {
        background: rgba(10, 15, 30, 0.75) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px;
        padding: 35px !important;
        max-width: 550px;
        margin: 5% auto !important;
        box-shadow: 0 0 40px rgba(56, 189, 248, 0.25), inset 0 0 15px rgba(56, 189, 248, 0.1);
        position: relative;
        z-index: 999;
    }
    
    .terminal-header {
        font-family: 'Courier New', monospace;
        color: #38BDF8;
        font-size: 13px;
        letter-spacing: 2px;
        margin-bottom: 20px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(56, 189, 248, 0.2);
        padding-bottom: 8px;
    }

    /* Top-Secret Encrypted CEO container card */
    .ceo-terminal {
        background: rgba(11, 19, 43, 0.65) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px !important;
        padding: 25px !important;
        position: relative;
        z-index: 10;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.15);
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
        text-shadow: 0 0 8px rgba(248,250,252,0.15);
    }
    
    .main-title { font-size: 44px; font-weight: 800; color: #F8FAFC; text-shadow: 0 0 25px rgba(56,189,248,0.6); position: relative; z-index: 10; }
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px dashed rgba(56, 189, 248, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌌 LIVE HIGH-VELOCITY SPACE FIELD & PHOTON COMET MATRIX ENGINE
st.components.v1.html("""
<canvas id="plasmaCometCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #020409; z-index: -999; pointer-events: none;"></canvas>
<script>
    const canvas = document.getElementById('plasmaCometCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const spaceDust = [];
    for(let i = 0; i < 350; i++) {
        spaceDust.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 1.8,
            sparkle: Math.random()
        });
    }

    let realComets = [
        { x: Math.random() * canvas.width, y: -100, dx: -7, dy: 7, size: 4, flare: '#38BDF8', glow: 'rgba(56,189,248,0.4)' },
        { x: Math.random() * canvas.width + 400, y: -100, dx: -9, dy: 9, size: 3, flare: '#F43F5E', glow: 'rgba(244,63,94,0.4)' },
        { x: Math.random() * canvas.width - 300, y: -100, dx: -6, dy: 6, size: 5, flare: '#A855F7', glow: 'rgba(168,85,247,0.4)' },
        { x: Math.random() * canvas.width + 100, y: -100, dx: -11, dy: 11, size: 2.5, flare: '#F59E0B', glow: 'rgba(245,158,11,0.4)' }
    ];

    function renderCosmos() {
        ctx.fillStyle = 'rgba(2, 4, 9, 0.3)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let particle of spaceDust) {
            ctx.fillStyle = `rgba(255, 255, 255, ${particle.sparkle})`;
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            ctx.fill();
            particle.sparkle += (Math.random() - 0.5) * 0.04;
            if(particle.sparkle < 0.1) particle.sparkle = 0.1;
            if(particle.sparkle > 1) particle.sparkle = 1;
        }

        for(let comet of realComets) {
            ctx.save();
            let cometGradient = ctx.createLinearGradient(comet.x, comet.y, comet.x - comet.dx * 18, comet.y - comet.dy * 18);
            cometGradient.addColorStop(0, '#FFFFFF');
            cometGradient.addColorStop(0.15, comet.flare);
            cometGradient.addColorStop(1, 'transparent');

            ctx.shadowColor = comet.flare;
            ctx.shadowBlur = 18;

            ctx.strokeStyle = cometGradient;
            ctx.lineWidth = comet.size;
            ctx.lineCap = 'round';
            ctx.beginPath();
            ctx.moveTo(comet.x, comet.y);
            ctx.lineTo(comet.x - comet.dx * 16, comet.y - comet.dy * 16);
            ctx.stroke();
            ctx.restore();

            comet.x += comet.dx;
            comet.y += comet.dy;

            if(comet.y > canvas.height + 200 || comet.x < -200 || comet.x > canvas.width + 200) {
                comet.x = Math.random() * canvas.width + canvas.width/3;
                comet.y = -100;
                comet.dy = Math.random() * 5 + 6;
                comet.dx = -comet.dy;
            }
        }
        requestAnimationFrame(renderCosmos);
    }
    renderCosmos();
</script>
""", height=0, scrolling=False)

# 🔒 HIGH-SECURITY SERVER DATABASE EMULATION LAYER
if "master_username" not in st.session_state: st.session_state["master_username"] = None
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

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
                st.session_state["master_username"] = setup_user.strip()
                st.session_state["master_password"] = setup_pass
                st.session_state["authenticated"] = True
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

# 🚀 RUN LIVE PLATFORM DASHBOARD IF BOTH PARAMETERS MATCH (CONTINUED)
if secure_gate_protocol():
    # Narrow sidebar configuration with dynamic profile greeting
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


