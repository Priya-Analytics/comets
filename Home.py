import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="comets | Infinite Space Hub", layout="wide", page_icon="☄️")

# ☄️ INJECT COMPACT GLOW COMPONENT OVERLAY STYLES
st.markdown("""
<style>
    .stApp {
        background: transparent !important;
    }
    html, body {
        background-color: #020306 !important;
    }
    
    /* Sleek container for the Hidden CEO terminal */
    .ceo-terminal {
        background: rgba(11, 19, 43, 0.6) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px !important;
        padding: 30px !important;
        position: relative;
        z-index: 10;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.15);
        margin-top: 20px;
    }
    
    .ceo-title {
        color: #38BDF8 !important;
        font-family: 'Courier New', monospace;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 18px;
        margin-bottom: 15px;
    }
    
    .quote-box {
        font-family: 'Georgia', serif;
        font-style: italic;
        color: #F8FAFC;
        font-size: 20px;
        line-height: 1.6;
        border-left: 4px solid #F43F5E;
        padding-left: 20px;
        margin: 20px 0;
        text-shadow: 0 0 10px rgba(248,250,252,0.2);
    }
    
    .main-title { font-size: 42px; font-weight: 800; color: #F8FAFC; text-shadow: 0 0 20px rgba(56,189,248,0.5); position: relative; z-index: 10; }
    
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px dashed rgba(56, 189, 248, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🌌 LIVE JAVASCRIPT SPACE FIELD & FALLING COMET SIMULATOR 
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

# 🔒 ROBUST CUSTOM AUTH CHECKS
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
    st.sidebar.markdown("# ☄️ comets")
    st.sidebar.markdown("---")
    
    uploaded_file = st.sidebar.file_uploader(
        label="", 
        type=["csv", "xlsx"],
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Secure Terminal / Log Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    st.markdown("<h1 class='main-title'>☄️ comets: Orbit Control Center</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                custom_df = pd.read_csv(uploaded_file)
            else:
                custom_df = pd.read_excel(uploaded_file)
                
            st.markdown(f"### 📂 Active Scratchpad Data: `{uploaded_file.name}`")
            st.dataframe(custom_df, use_container_width=True)
            
            st.markdown("### 🐍 Python Execution Terminal (Uploaded Sheet Context)")
            custom_code = st.text_area(
                "Write data manipulation code here (use `custom_df` variable):", 
                value="# Basic description statistics example\nst.write(custom_df.describe())"
            )
            if st.button("Execute Upload Logic Stream"):
                exec(custom_code, {"custom_df": custom_df, "pd": pd, "st": st})
            st.markdown("---")
            
        except Exception as e:
            st.error(f"Failed to process spreadsheet file: {e}")

    # 🔒 TOP-SECRET: HIDDEN CEO QUOTES TERMINAL AREA
    st.markdown("""
    <div class="ceo-terminal">
        <div class="ceo-title">🔒 RESTRICTED DIRECTIVE: ENCRYPTED EXECUTIVE LOGS</div>
        <p style="color: #94A3B8; font-size: 14px; margin-bottom: 20px;">
            Intercepting internal quantum channels. Strategic directives for comets network nodes are buffered below.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # List of strategic executive analyst quotes
    ceo_quotes = [
        '"In global logistics, a delay in transit isn\'t a resource shortage—it\'s an information asymmetry problem. Optimize visibility, and speed takes care of itself." — Chief Executive Officer',
        '"The comets network doesn\'t build traditional tracks; we build resilient, self-healing supply pipelines across complex dimensions." — Chief Logistics Officer',
        '"A master data analyst doesn\'t stare at lagging indices. They forecast structural bottlenecks before manufacturing nodes throw failure codes." — Chief Technology Director',
        '"Efficiency is born when lead time drop matrices sync perfectly with dynamic automated replenishment variables." — Executive Operations Board',
        '"True supply chain optimization isn\'t about cutting total route costs. It is about building flexibility to survive localized network collapses." — Chief Procurement Officer'
    ]
    
    # Handle random generation cache loops using simple session states
    if "current_quote" not in st.session_state:
        st.session_state["current_quote"] = ceo_quotes[0]
        
    if st.button("🔌 Decrypt Next Command Directive"):
        st.session_state["current_quote"] = random.choice(ceo_quotes)
        st.rerun()
        
    st.markdown(f'<div class="quote-box">{st.session_state["current_quote"]}</div>', unsafe_allow_html=True)
