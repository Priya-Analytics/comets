import streamlit as st
import pandas as pd
from data_warehouse import get_freight_audit_data

st.set_page_config(page_title="Freight Audit | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Supply Chain Finance")

st.title("💸 Freight Cost Audit Matrix")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** Finance wants to flag billing leakage where the carrier's final invoice invoice exceeds estimates.
* **Your Assignment:** Write a script to calculate the cost variance (`Billed_Cost` - `Estimated_Cost`) and flag discrepancies over $200.
""")

freight_df = get_freight_audit_data()
st.dataframe(freight_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Calculate absolute variance percentage
freight_df['Variance_Pct'] = ((freight_df['Billed_Cost'] - freight_df['Estimated_Cost']) / freight_df['Estimated_Cost']) * 100
st.dataframe(freight_df[['Invoice_ID', 'Load_ID', 'Variance_Pct']])
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"freight_df": freight_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
