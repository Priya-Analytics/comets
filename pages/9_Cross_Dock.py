import streamlit as st
import pandas as pd
from data_warehouse import get_crossdock_data

st.set_page_config(page_title="Cross-Dock | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Hub Warehousing")

st.title("🏬 Facility Cross-Dock & Yard Operations")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** The terminal manager wants to audit trailer dwell time to keep inbound bay doors clear.
* **Your Assignment:** Query out trailers that spent more than 4 hours idling in the yard (`Dwell_Time_Hours` > 4.0).
""")

crossdock_df = get_crossdock_data()
st.dataframe(crossdock_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Group the average trailer unload time by carrier company
avg_unload = crossdock_df.groupby('Inbound_Carrier')['Unload_Duration_Min'].mean().reset_index()
st.dataframe(avg_unload)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"crossdock_df": crossdock_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
