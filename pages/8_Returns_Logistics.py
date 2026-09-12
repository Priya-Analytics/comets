import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import pandas as pd
from data_warehouse import get_returns_data

st.set_page_config(page_title="Returns Logistics | coments", layout="wide")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.title("🔄 Reverse Logistics & Customer Returns")
st.markdown("---")

returns_df = get_returns_data()
st.dataframe(returns_df, use_container_width=True)
user_script = st.text_area("Input script context:", value="st.write(returns_df.head())")
if st.button("Run Routine Engine"):
    try: exec(user_script, {"returns_df": returns_df, "pd": pd, "st": st})
    except Exception as err: st.error(f"Error: {err}")
