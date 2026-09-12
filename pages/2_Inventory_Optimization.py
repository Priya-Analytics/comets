import streamlit as st
import pandas as pd
from data_warehouse import get_inventory_data

st.set_page_config(page_title="Inventory Management | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Operations & Flow")

st.title("📦 Inventory Optimization Sandbox")
st.markdown("---")

st.subheader("📋 Core Scenario & Objective")
st.info("""
**Business Challenge:** The inventory controller wants to prevent deadstock while minimizing warehousing expenses.
* **Your Assignment:** Write a Python routine to execute ABC classification based on annual financial velocity (`Annual_Qty_Sold` * `Unit_Cost_USD`).
""")

inventory_df = get_inventory_data()
st.dataframe(inventory_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Calculate total valuation of on-hand stock
inventory_df['Stock_Value'] = inventory_df['Current_Stock_Level'] * inventory_df['Unit_Cost_USD']
total_valuation = inventory_df['Stock_Value'].sum()
print(f"Total Facility Valuation: ${total_valuation:,.2f}")
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"inventory_df": inventory_df, "pd": pd}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully. Check system runtime window logs.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
