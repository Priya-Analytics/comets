import streamlit as st
import pandas as pd
from data_warehouse import get_manufacturing_data

st.set_page_config(page_title="Manufacturing | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Plant Operations")

st.title("🏭 Plant Production & Line Logs")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** Plant operations wants to study production line performance by monitoring assembly line downtime.
* **Your Assignment:** Calculate total line downtime minutes (`Planned_Run_Time_Min` - `Actual_Run_Time_Min`) and output target efficiency.
""")

mfg_df = get_manufacturing_data()
st.dataframe(mfg_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Find shifts where produced units fell below target yield
underperforming_shifts = mfg_df[mfg_df['Produced_Units'] < mfg_df['Target_Units']]
st.dataframe(underperforming_shifts)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"mfg_df": mfg_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
