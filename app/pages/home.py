import streamlit as st

from core.config import path
from core.utils import page, make_style

make_style("style.css")

st.markdown("""
    <h2 style='text-align:center'>
        Automation Hub
    </h2>
    """, unsafe_allow_html=True)

st.image(path.IMAGE_PATH+"background.gif", use_column_width=True)

st.markdown("""
    <h5 style='text-align:center'>
        Automation Hub is a web-based platform to programmatically develop, operate, and monitor data pipelines.
    </h5>
    """, unsafe_allow_html=True)

col5 = st.columns(5)

with col5[2]:
    if st.button("Getting started", type='primary'):
        st.switch_page(page.documentation)