import streamlit as st
import pandas as pd
import numpy as np
import time
from transform import transform_android_app

st.set_page_config(
    page_title="Chat",
    page_icon="🌐",
)

if "path" in st.session_state:
    st.warning("An app has been generated. Redirecting you to the code page...")
    time.sleep(3)
    st.switch_page("pages/code.py")

with st.form("idea_form"):
   st.write("# Plan your idea here")
   intent = st.text_area("Your next big idea is brewing...")
   submit = st.form_submit_button('Generate!')

if submit:
    st.success("Generating your app...")
    st.session_state.path = transform_android_app(intent)
    st.switch_page("pages/code.py")
