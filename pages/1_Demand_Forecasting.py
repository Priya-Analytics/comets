import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Demand Forecasting | coments", layout="wide")

# 🔒 REUSE RECONFIGURED PASSWORD GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()
    
# Persistent branding sidebar
st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Planning & Forecasting")

st.title("📈 Demand Forecasting Matrix")
st.markdown("---")

st.subheader("📋 Scenario Brief")
st.warning("Target: Run analytical summaries to determine seasonal inventory velocity spikes.")

# Data Gen
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")
mock_data = pd.DataFrame({
    "Date": dates.strftime("%Y-%m-%d"),
    "SKU_ID": ["SKU-1001" if i%2==0 else "SKU-1002" for i in range(30)],
    "Product_Category": ["Electronics" if i%2==0 else "Apparel" for i in range(30)],
    "Historical_Orders": np.random.randint(50, 200, size=30),
    "Promotion_Active": np.random.choice([0, 1], size=30, p=[0.7, 0.3])
})

st.dataframe(mock_data, use_container_width=True)

# Python Script Sandbox
st.subheader("🐍 Script Execution Terminal")
code_input = st.text_area("Input Python code for target aggregation:", 
                          value="# Compute mathematical summary stats\nsummary = mock_data['Historical_Orders'].describe()\nprint(summary)")

if st.button("Execute Stream"):
    try:
        local_vars = {"mock_data": mock_data, "pd": pd, "np": np}
        exec(code_input, {}, local_vars)
        st.success("Execution string compiled without errors. (Outputs sent to system log)")
    except Exception as e:
        st.error(f"Compile Error: {e}")