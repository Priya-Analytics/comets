import streamlit as st
import pandas as pd
from data_warehouse import get_omnichannel_data

st.set_page_config(page_title="Omnichannel | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Fulfillment Metrics")

st.title("🛒 Omnichannel E-Commerce Order Flow")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** The digital team wants to evaluate velocity speed-to-shelf times by finding shipping manifest lags.
* **Your Assignment:** Calculate total processing time (`Pick_Time_Sec` + `Pack_Time_Sec` + `Courier_Manifest_Sec`) for every order line item.
""")

omni_df = get_omnichannel_data()
st.dataframe(omni_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Calculate packing error rates by fulfillment zone
error_summary = omni_df.groupby('Fulfillment_Zone')['Error_Flag'].sum().reset_index()
st.dataframe(error_summary)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"omni_df": omni_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
