import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Demand Forecasting | coments", layout="wide")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.title("📈 Demand Forecasting Matrix")
st.markdown("---")

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
code_input = st.text_area("Input Python code:", value="st.write(mock_data.describe())")
if st.button("Execute Stream"):
    try: exec(code_input, {"mock_data": mock_data, "pd": pd, "np": np, "st": st})
    except Exception as e: st.error(f"Error: {e}")
