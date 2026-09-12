import streamlit as st
import pandas as pd
from data_warehouse import get_carrier_data

st.set_page_config(page_title="Carrier Performance | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Logistics & Transit")

st.title("🚢 Carrier Performance Matrix")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** The freight team needs to monitor carrier SLA compliance and flag recurring route delays.
* **Your Assignment:** Calculate the On-Time Delivery Rate (OTD%) for each carrier where `Actual_Delivery_Days` <= `SLA_Delivery_Days`.
""")

carrier_df = get_carrier_data()
st.dataframe(carrier_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Find rows where delivery took longer than SLA contract
delayed_shipments = carrier_df[carrier_df['Actual_Delivery_Days'] > carrier_df['SLA_Delivery_Days']]
st.dataframe(delayed_shipments)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"carrier_df": carrier_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
