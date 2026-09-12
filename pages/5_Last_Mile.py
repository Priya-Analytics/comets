import streamlit as st
import pandas as pd
from data_warehouse import get_lastmile_data

st.set_page_config(page_title="Last-Mile Delivery | coments", layout="wide")

# 🔒 SECURITY ACCESS GATE
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.sidebar.info("Section: Last-Mile Distribution")

st.title("🗺️ Last-Mile Courier Operations")
st.markdown("---")

st.subheader("📋 Scenario Brief & Objective")
st.info("""
**Business Challenge:** Fleet management wants to optimize courier dispatch by evaluating vehicle fuel consumption parameters.
* **Your Assignment:** Calculate fuel efficiency metrics like Kilometers per Liter (`Route_Distance_KM` / `Fuel_Consumed_Liters`).
""")

lastmile_df = get_lastmile_data()
st.dataframe(lastmile_df, use_container_width=True)

st.subheader("🐍 Code Matrix Console")
user_script = st.text_area("Input script context:", 
value="""# Example: Find all low-performing routes with a customer rating below 4.0
low_ratings = lastmile_df[lastmile_df['Customer_Rating'] < 4.0]
st.dataframe(low_ratings)
""")

if st.button("Run Routine Engine"):
    try:
        local_scope = {"lastmile_df": lastmile_df, "pd": pd, "st": st}
        exec(user_script, {}, local_scope)
        st.success("Routine executed successfully.")
    except Exception as err:
        st.error(f"Runtime Exception: {err}")
