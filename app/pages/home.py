import streamlit as st

from core.config import path
from core.utils import page, add_heading, use_style

add_heading("Automation Hub", tag="h2", style={"text-align": "center"})

st.image(path.IMAGE_PATH+"background.gif", use_column_width=True)

add_heading("Automation Hub is a web-based platform to programmatically develop, operate, and monitor data pipelines.",
            tag="h5", style={"text-align": "center"})

col = st.columns(5)
with col[2]:
    use_style("botton.css")
    if st.button("Getting started", type='primary', use_container_width=True):
        st.switch_page(page.documentation)

add_heading("Principles", tag="h4", style={"text-align": "center"})

image_col1 = st.columns(6)
text_col1 = st.columns(2)
with image_col1[1]:
    st.image(path.IMAGE_PATH+"abstraction.png", use_column_width=True)
with text_col1[0]:
    add_heading("Abstraction", tag="h5", style={"text-align": "center"})
    add_heading("Hide technical complexity, allowing users to focus on business logic.",
                tag="h6", style={"text-align": "center"})
with image_col1[4]:
    st.image(path.IMAGE_PATH+"flexibility.png", use_column_width=True)
with text_col1[1]:
    add_heading("Flexibility", tag="h5", style={"text-align": "center"})
    add_heading("Support various data sources, sinks, and pipeline structures to accommodate different business needs.",
                tag="h6", style={"text-align": "center"})

image_col2 = st.columns(6)
text_col2 = st.columns(2)
with image_col2[1]:
    st.image(path.IMAGE_PATH+"reusability.png", use_column_width=True)
with text_col2[0]:
    add_heading("Reusability", tag="h5", style={"text-align": "center"})
    add_heading("Enable the creation of reusable data pipeline components for efficient development and maintenance.",
                tag="h6", style={"text-align": "center"})
with image_col2[4]:
    st.image(path.IMAGE_PATH+"extensibility.png", use_column_width=True)
with text_col2[1]:
    add_heading("Extensibility", tag="h5", style={"text-align": "center"})
    add_heading("Allow for easy customization and integration with other systems to meet evolving requirements.",
                tag="h6", style={"text-align": "center"})