import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Configure wide page matrix layout
st.set_page_config(page_title="comets | Infinite Space Hub", layout="wide", page_icon="☄️")

# ☄️ INJECT COMPACT GLOW COMPONENT OVERLAY STYLES
st.markdown("""
<style>
    /* Force main app background to look hidden or transparent so the canvas stars show through */
    .stApp {
        background: transparent !important;
    }
    
    html, body {
        background-color: #020306 !important;
    }

    /* 🛠️ NARROW LEFT SIDEBAR FOOTPRINT WIDTH */
    [data-testid="stSidebar"] {
        min-width: 190px !important;
        max-width: 230px !important;
        background-color: rgba(6, 9, 15, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Glowing container for the Hidden CEO terminal */
    .ceo-terminal {
        background: rgba(11, 19, 43, 0.65) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px !important;
        padding: 25px !important;
        position: relative;
        z-index: 10;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.15);
        margin-top: 10px;
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

    /* Right widget side container panels */
    .right-widget-panel {
        background: rgba(14, 20, 38, 0.65) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 14px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        margin-bottom: 20px;
        position: relative;
        z-index: 10;
    }
    
    .widget-title {
        color: #38BDF8 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 12px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(56, 189, 248, 0.2);
        padding-bottom: 6px;
    }
    
    .main-title { font-size: 42px; font-weight: 800; color: #F8FAFC; text-shadow: 0 0 20px rgba(56,189,248,0.5); position: relative; z-index: 10; }
    
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px dashed rgba(56, 189, 248, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌌 LIVE JAVASCRIPT SPACE FIELD & FALLING COMET CANVAS SIMULATOR 
st.components.v1.html("""
<canvas id="spaceCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #020306; z-index: -999; pointer-events: none;"></canvas>
<script>
    const canvas = document.getElementById('spaceCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const stars = [];
    for(let i = 0; i < 400; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 2,
            opacity: Math.random()
        });
    }

    let comets = [
        { x: Math.random() * canvas.width, y: -50, speedX: -6, speedY: 6, length: 150, color: '#38BDF8' },
        { x: Math.random() * canvas.width + 300, y: -50, speedX: -8, speedY: 8, length: 110, color: '#F43F5E' },
        { x: Math.random() * canvas.width - 200, y: -50, speedX: -5, speedY: 5, length: 130, color: '#A855F7' }
    ];

    function draw() {
        ctx.fillStyle = '#020306';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let star of stars) {
            ctx.fillStyle = `rgba(255, 255, 255, ${star.opacity})`;
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();
            star.opacity += (Math.random() - 0.5) * 0.04;
            if(star.opacity < 0.1) star.opacity = 0.1;
            if(star.opacity > 1) star.opacity = 1;
        }

        for(let comet of comets) {
            let gradient = ctx.createLinearGradient(comet.x, comet.y, comet.x - comet.speedX * 15, comet.y - comet.speedY * 15);
            gradient.addColorStop(0, '#FFFFFF');
            gradient.addColorStop(0.15, comet.color);
            gradient.addColorStop(1, 'transparent');

            ctx.strokeStyle = gradient;
            ctx.lineWidth = 3.5;
            ctx.lineCap = 'round';
            ctx.beginPath();
            ctx.moveTo(comet.x, comet.y);
            ctx.lineTo(comet.x - comet.speedX * 15, comet.y - comet.speedY * 15);
            ctx.stroke();

            comet.x += comet.speedX;
            comet.y += comet.speedY;

            if(comet.y > canvas.height + 150 || comet.x < -150 || comet.x > canvas.width + 150) {
                comet.x = Math.random() * canvas.width + canvas.width/4;
                comet.y = -50;
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
</script>
""", height=0, scrolling=False)

# 🔒 ROBUST SECURITY LAYER CHECKS
if "master_password" not in st.session_state: st.session_state["master_password"] = None
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False

def check_password():
    if st.session_state["master_password"] is None:
        st.markdown("<h2 class='main-title'>☄️ comets Security Matrix Configuration</h2>", unsafe_allow_html=True)
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
    # Left Sidebar layout containing your document uploader dropzone box
    st.sidebar.markdown("# ☄️ comets")
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader(label="", type=["csv", "xlsx"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Terminal / Log Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    # 🛠️ ASYMMETRIC GRID DESIGN INTERFACES
    main_left_col, right_panel_col = st.columns([0.70, 0.30], gap="large")

    with main_left_col:
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
            except Exception as e: st.error(f"Failed to process file: {e}")

                # 🔒 TOP-SECRET: HIDDEN CEO QUOTES TERMINAL AREA (CONTINUED)
        ceo_quotes = [
            '"In global logistics, a delay in transit isn\'t a resource shortage—it\'s an information asymmetry problem. Optimize visibility, and speed takes care of itself." — Chief Executive Officer',
            '"The comets network doesn\'t build traditional tracks; we build resilient, self-healing supply pipelines across complex dimensions." — Chief Logistics Officer',
            '"A master data analyst doesn\'t stare at lagging indices. They forecast structural bottlenecks before manufacturing nodes throw failure codes." — Chief Technology Director',
            '"Efficiency is born when lead time drop matrices sync perfectly with dynamic automated replenishment variables." — Executive Operations Board',
            '"True supply chain optimization isn\'t about cutting total route costs. It is about building flexibility to survive localized network collapses." — Chief Procurement Officer'
        ]
        
        # 🔄 Initialize session states so data stays safe during click refreshes
        if "current_quote" not in st.session_state:
            st.session_state["current_quote"] = random.choice(ceo_quotes)
            
        # 🔌 Decryption command control loop engine
        if st.button("🔌 Decrypt Next Command Directive"):
            st.session_state["current_quote"] = random.choice(ceo_quotes)
            st.rerun()
            
        # Render the custom formatted quotes container box block onto the viewport screen
        st.markdown(f'<div class="quote-box">{st.session_state["current_quote"]}</div>', unsafe_allow_html=True)

    # 🛰️ RIGHT COLUMN METRICS PANELS
    with right_panel_col:
        # Streamlined Chrono-Telemetry Panel (Only Time, Date, and Calendar)
        st.markdown('<div class="right-widget-panel">', unsafe_allow_html=True)
        st.markdown('<div class="widget-title">🛰️ Chrono-Telemetry Data</div>', unsafe_allow_html=True)
        
        time_str = datetime.now().strftime("%I:%M:%S %p")
        date_str = datetime.now().strftime("%A, %B %d, %Y")
        
        st.markdown(f"**⏰ Station Time:** `{time_str}`")
        st.markdown(f"**📅 Current Date:** `{date_str}`")
        
        selected_date = st.date_input("📅 Select Calendar Target View:", value=datetime.now(), key="space_calendar")
        st.markdown(f"<p style='font-size:11px; color:#8B949E; margin-top:5px;'>Active Orbit: Year {selected_date.year}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
