import streamlit as st

st.set_page_config(page_title="coments | SC Sandbox", layout="wide", page_icon="🚚")

# Initialize persistent session states if they don't exist yet
if "master_password" not in st.session_state:
    st.session_state["master_password"] = None  # Start with no password set

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 🔐 SECURITY FUNCTIONS
def check_password():
    # SCENARIO A: No password has been set yet (First time setup)
    if st.session_state["master_password"] is None:
        st.subheader("⚙️ coments Initial Security Configuration")
        st.info("No password found in memory. Please configure your custom access key below.")
        
        new_pass = st.text_input("Create Your Private Master Password:", type="password", key="setup_pass_input")
        confirm_pass = st.text_input("Confirm Your Private Master Password:", type="password", key="setup_confirm_input")
        
        if st.button("Set Master Encryption Lock"):
            if new_pass == "":
                st.error("Password cannot be blank!")
            elif new_pass == confirm_pass:
                st.session_state["master_password"] = new_pass
                st.session_state["authenticated"] = True
                st.success("🔒 Master password registered successfully! Refreshing app...")
                st.rerun()
            else:
                st.error("❌ Passwords do not match! Please check your spelling.")
        return False

    # SCENARIO B: User is already logged in successfully
    if st.session_state["authenticated"]:
        return True

    # SCENARIO C: Password exists, prompt the user to log in
    st.subheader("🏢 coments Secure Access Gateway")
    input_pass = st.text_area("Input private analyst credentials:", type="password", key="login_pass_input")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Verify Key"):
            if input_pass == st.session_state["master_password"]:
                st.session_state["authenticated"] = True
                st.success("Access Granted.")
                st.rerun()
            else:
                st.error("❌ Invalid Access Key.")
                
    with col2:
        # 🔑 FORGOT PASSWORD ROUTINE TRIGGER
        if st.button("❓ Forgot Password / Reset Key"):
            st.session_state["master_password"] = None
            st.session_state["authenticated"] = False
            st.warning("⚠️ Access keys wiped from container memory. Please create a new one below.")
            st.rerun()
            
    return False

# 🚀 CORE PLATFORM LAYOUT EXECUTION
if check_password():
    # Cohesive Persistent Sidebar Branding
    st.sidebar.markdown("# 🏢 coments")
    st.sidebar.markdown("*Personal Analytics Sandbox*")
    
    # Let user log out or reset from the sidebar if desired
    if st.sidebar.button("🔒 Lock Portal / Log Out"):
        st.session_state["authenticated"] = False
        st.rerun()

    st.title("📟 coments: Supply Chain Analyst Hub")
    st.markdown("---")
    st.markdown("""
    ### Welcome to your personal practice workspace.
    This platform is strictly restricted for **private use** to test technical workflows, execute SQL/Python queries, review API documentation, and audit operational data models.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="SQL Databases", value="Ready to Connect")
    with col2:
        st.metric(label="Python Sandbox", value="Active Environment")
    with col3:
        st.metric(label="Power BI Matrix", value="Ready to Embed")
