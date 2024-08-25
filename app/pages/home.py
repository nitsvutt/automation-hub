import streamlit as st

from core.config import path
from core.utils import page, add_heading, use_style

add_heading("Automation Hub", tag="h2", style={"text-align": "center"})

st.image(path.IMAGE_PATH+"background.gif", use_column_width=True)

add_heading("Automation Hub is a web-based platform to programmatically develop, operate, and monitor data pipelines.",
            tag="h5", style={"text-align": "center"})

col = st.columns([1]*5)
with col[2]:
    use_style("botton.css")
    if st.button("Getting started", type='primary', use_container_width=True):
        st.switch_page(page.documentation)

add_heading("Principles", tag="h3", style={"text-align": "center"})