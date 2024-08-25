import streamlit as st

from core.config import path
from core.utils import page, add_tag, use_style

add_tag("Automation Hub", tag="h2", style={"text-align": "center"})

st.image(path.IMAGE_PATH+"background.gif", use_column_width=True)

add_tag("Automation Hub is a web-based platform to programmatically develop, operate, and monitor data pipelines.",
            tag="p", style={"text-align": "center", "color": "grey", "font-size": "115%"})

col = st.columns(5)
with col[2]:
    use_style("botton.css")
    if st.button("Getting started", type='primary', use_container_width=True):
        st.switch_page(page.documentation)

add_tag("Principles", tag="h4", style={"text-align": "center"})

image_col1 = st.columns(6)
text_col1 = st.columns(2)
with image_col1[1]:
    st.image(path.IMAGE_PATH+"abstraction.png", use_column_width=True)
with text_col1[0]:
    add_tag("Abstraction", tag="h6", style={"text-align": "center"})
    add_tag("Hide technical complexity, allowing users to focus on business logic.",
                tag="p", style={"text-align": "center", "color": "grey"})
with image_col1[4]:
    st.image(path.IMAGE_PATH+"flexibility.png", use_column_width=True)
with text_col1[1]:
    add_tag("Flexibility", tag="h6", style={"text-align": "center"})
    add_tag("Support various data sources, sinks, and pipeline structures to accommodate different business needs.",
                tag="p", style={"text-align": "center", "color": "grey"})

image_col2 = st.columns(6)
text_col2 = st.columns(2)
with image_col2[1]:
    st.image(path.IMAGE_PATH+"reusability.png", use_column_width=True)
with text_col2[0]:
    add_tag("Reusability", tag="h6", style={"text-align": "center"})
    add_tag("Enable the creation of reusable data pipeline components for efficient development and maintenance.",
                tag="p", style={"text-align": "center", "color": "grey"})
with image_col2[4]:
    st.image(path.IMAGE_PATH+"extensibility.png", use_column_width=True)
with text_col2[1]:
    add_tag("Extensibility", tag="h6", style={"text-align": "center"})
    add_tag("Allow for easy customization and integration with other systems to meet evolving requirements.",
                tag="p", style={"text-align": "center", "color": "grey"})
    
add_tag("Features", tag="h4", style={"text-align": "center"})

image_col1 = st.columns(6)
text_col1 = st.columns(2)
with image_col1[1]:
    st.image(path.IMAGE_PATH+"pure_sql.png", use_column_width=True)
with text_col1[0]:
    add_tag("Pure SQL", tag="h6", style={"text-align": "center"})
    add_tag("No programming language is required. Use Standard SQL syntax and add some configs to create your data pipelines.",
                tag="p", style={"text-align": "center", "color": "grey"})
with image_col1[4]:
    st.image(path.IMAGE_PATH+"useful_ui.png", use_column_width=True)
with text_col1[1]:
    add_tag("Useful UI", tag="h6", style={"text-align": "center"})
    add_tag("Create, config, start, and monitor your pipelines in one central user interface.",
                tag="p", style={"text-align": "center", "color": "grey"})

image_col2 = st.columns(6)
text_col2 = st.columns(2)
with image_col2[1]:
    st.image(path.IMAGE_PATH+"robust_integrations.png", use_column_width=True)
with text_col2[0]:
    add_tag("Robust Integrations", tag="h6", style={"text-align": "center"})
    add_tag("Support all data source and sink types provided by your company.",
                tag="p", style={"text-align": "center", "color": "grey"})
with image_col2[4]:
    st.image(path.IMAGE_PATH+"easy_to_use.png", use_column_width=True)
with text_col2[1]:
    add_tag("Easy to Use", tag="h6", style={"text-align": "center"})
    add_tag("Anyone with SQL knowledge can deploy a data pipeline.",
                tag="p", style={"text-align": "center", "color": "grey"})

add_tag("Contact me", tag="h4", style={"text-align": "center"})

contact_col = st.columns(15)
with contact_col[6]:
    add_tag(f"<img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' />",
            tag="a", additional={"href": "https://linkedin.com/in/nitsvutt"})
with contact_col[7]:
    add_tag("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png' />",
            tag="a", additional={"href": "mailto:nitsvutt@gmail.com"})
with contact_col[8]:
    add_tag("<img src='https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg' />",
            tag="a", additional={"href": "https://instagram.com/nitsvutt"})
    