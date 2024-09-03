import streamlit as st
from datetime import datetime
import pytz

from core.config import dt_format, path

class Page():
    def __init__(self):
        self.home = st.Page(path.PAGE_PATH + "home.py", title="Home", icon=":material/home:")
        self.dashboard = st.Page(path.PAGE_PATH + "dashboard.py", title="Dashboard", icon=":material/dashboard:")
        self.pipeline = st.Page(path.PAGE_PATH + "pipeline.py", title="Pipeline", icon=":material/water_pump:")
        self.documentation = st.Page(path.PAGE_PATH + "documentation.py", title="Documentation", icon=":material/description:")

def add_tag(text: str, tag: str, additional: dict = {}, style: dict = {}):
    heading_font_size = {
        'h1': '220%',
        'h2': '200%',
        'h3': '180%',
        'h4': '160%',
        'h5': '140%',
        'h6': '120%'
    }
    font_size = heading_font_size.get(tag, None)
    if font_size:
        style.update({"font-size": font_size})
        style.update({"font-weight": "bold"})
        tag = 'p'
    if additional:
        all_additional = ' '.join([key + '=' + value for key, value in additional.items()])
    else:
        all_additional = ""
    if style:
        all_style = "style='" + ';'.join([key + ':' + value for key, value in style.items()]) + "'"
    else:
        all_style = ""
    st.markdown(f"<{tag} {all_additional} {all_style}> {text} </{tag}>", unsafe_allow_html=True)

def use_style(css_file: str):
    with open(path.CSS_PATH + css_file) as file:
        css = file.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def current_sysdate():
    return datetime.now(pytz.timezone(dt_format.TIMEZONE)).strftime(dt_format.DATE_FORMAT)

def current_systime():
    return datetime.now(pytz.timezone(dt_format.TIMEZONE)).strftime(dt_format.DATETIME_FORMAT)

page = Page()