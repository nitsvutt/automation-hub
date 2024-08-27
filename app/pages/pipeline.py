import streamlit as st

from core.config import path
from core.utils import page, add_tag, use_style

add_tag("Pipeline", tag="h1", style={"text-align": "center"})

col = st.columns(3)
with col[0]:
    use_style("botton.css")
    create_pipeline = st.button(":material/add_circle: Create pipeline", type='primary', use_container_width=True)

with col[1]:
    use_style("botton.css")
    update_pipeline = st.button(":material/edit: Update pipeline", type='primary', use_container_width=True)

with col[2]:
    use_style("botton.css")
    delete_pipeline = st.button(":material/delete: Delete pipeline", type='primary', use_container_width=True)

if create_pipeline:
    st.session_state["session_option"] = "create"
elif update_pipeline:
    st.session_state["session_option"] = "update"
elif delete_pipeline:
    st.session_state["session_option"] = "delete"

if "session_option" in st.session_state:
    if st.session_state["session_option"] == "create":
        # init title
        add_tag("Create pipeline", tag="h4", style={"text-align": "center"})
        add_tag("Pipeline indicator", tag="h6", style={"text-align": "left"})
        # input pipeline configuration
        pipeline_name = st.text_input(label = "Pipeline name:", key = "pipeline_name", value = "")
        pipeline_type = st.text_input(label="Pipeline type:", key = "pipeline_type", value="")
        # update pipeline configuration
        col = st.columns(3)
        with col[1]:
            use_style("botton.css")
            commit = st.button(":material/save: Commit", type='primary', use_container_width=True)
        if commit:
            input = {}
            input.update(
                {
                    "pipeline_name": st.session_state["pipeline_name"],
                    "pipeline_type": st.session_state["pipeline_type"]
                }
            )
            st.write(input)