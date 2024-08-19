import streamlit as st

home = st.Page("pages/home.py", title="Home", icon=":material/home:")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
pipeline = st.Page("pages/pipeline.py", title="Pipeline", icon=":material/water_pump:")

pg = st.navigation([home, dashboard, pipeline])

pg.run()