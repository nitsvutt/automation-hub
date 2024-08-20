import streamlit as st

from core.config import (
    PAGE_PATH
)

home = st.Page(PAGE_PATH+"home.py", title="Home", icon=":material/home:")
dashboard = st.Page(PAGE_PATH+"dashboard.py", title="Dashboard", icon=":material/dashboard:")
pipeline = st.Page(PAGE_PATH+"pipeline.py", title="Pipeline", icon=":material/water_pump:")

pg = st.navigation([home, dashboard, pipeline])

pg.run()