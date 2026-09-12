import streamlit as st
import pandas as pd
from data_warehouse import get_procurement_data

st.set_page_config(page_title="Procurement Risk | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Sourcing & Procurement")

st.title("🤝 Procurement & Supplier Risk Matrix")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** Sourcing must audit global component vendor quality metrics before signing new vendor contracts.
* **Your Assignment:** Calculate the defect rate percentage (`Defect_Qty` / `Order_Qty`) for each Supplier ID.
""")

procurement_df = get_procurement_data()
st.dataframe(procurement_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Calculate total spend per purchase order row
procurement_df['Total_Spend'] = procurement_df['Order_Qty'] * procurement_df['Unit_Price_USD']
st.dataframe(procurement_df[['PO_Number', 'Supplier_ID', 'Total_Spend']])
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"procurement_df": procurement_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
