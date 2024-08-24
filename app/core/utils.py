import streamlit as st
from datetime import datetime
import pytz

from core.config import env, path

class Page():
    def __init__(self):
        self.home = st.Page(path.PAGE_PATH+"home.py", title="Home", icon=":material/home:")
        self.dashboard = st.Page(path.PAGE_PATH+"dashboard.py", title="Dashboard", icon=":material/dashboard:")
        self.pipeline = st.Page(path.PAGE_PATH+"pipeline.py", title="Pipeline", icon=":material/water_pump:")
        self.documentation = st.Page(path.PAGE_PATH+"documentation.py", title="Documentation", icon=":material/description:")

def make_style(css_file: str):
    with open(path.CSS_PATH+css_file) as file:
        css = file.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def current_sysdate():
    return datetime.now(pytz.timezone(env.TIMEZONE)).strftime(env.DATE_FORMAT)

def current_systime():
    return datetime.now(pytz.timezone(env.TIMEZONE)).strftime(env.DATETIME_FORMAT)

page = Page()