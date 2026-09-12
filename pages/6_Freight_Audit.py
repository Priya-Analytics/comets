import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import pandas as pd
from data_warehouse import get_freight_audit_data

st.set_page_config(page_title="Freight Audit | coments", layout="wide")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔐 Please configure and log in on the Home page first to access this operational matrix.")
    st.stop()

st.sidebar.markdown("# 🏢 coments")
st.title("💸 Freight Cost Audit Matrix")
st.markdown("---")

freight_df = get_freight_audit_data()
st.dataframe(freight_df, use_container_width=True)
user_script = st.text_area("Input script context:", value="st.write(freight_df.head())")
if st.button("Run Routine Engine"):
    try: exec(user_script, {"freight_df": freight_df, "pd": pd, "st": st})
    except Exception as err: st.error(f"Error: {err}")
