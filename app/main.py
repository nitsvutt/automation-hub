import streamlit as st

from core.utils import page

pg = st.navigation([
    page.home,
    page.dashboard,
    page.pipeline,
    page.documentation
])

pg.run()