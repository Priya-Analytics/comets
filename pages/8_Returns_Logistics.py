import streamlit as st
import pandas as pd
from data_warehouse import get_returns_data

st.set_page_config(page_title="Returns Logistics | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Aftermarket Quality")

st.title("🔄 Reverse Logistics & Customer Returns")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** Customer support wants to classify the major pain points leading to cash refunds.
* **Your Assignment:** Calculate total loss value from returns grouped by `Return_Reason`.
""")

returns_df = get_returns_data()
st.dataframe(returns_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Identify items marked for immediate scrapping
scrap_items = returns_df[returns_df['Item_Condition'] == 'Scrap/Liquidate']
st.dataframe(scrap_items)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"returns_df": returns_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
