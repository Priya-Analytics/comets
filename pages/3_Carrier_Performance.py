import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import pandas as pd
from data_warehouse import get_carrier_data

st.set_page_config(page_title="Carrier Performance | coments", layout="wide")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.title("🚢 Carrier Performance Matrix")
st.markdown("---")

carrier_df = get_carrier_data()
st.dataframe(carrier_df, use_container_width=True)
user_script = st.text_area("Input script context:", value="st.write(carrier_df.head())")
if st.button("Run Routine Engine"):
    try: exec(user_script, {"carrier_df": carrier_df, "pd": pd, "st": st})
    except Exception as err: st.error(f"Error: {err}")
