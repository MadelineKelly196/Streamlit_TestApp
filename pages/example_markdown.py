import streamlit as st
st.set_page_config(page_title="MLOps",
                   page_icon=None,
                   layout= "centered",
                   initial_sidebar_state="auto",
                   menu_items=None
)

st.title("Streamlit: MLOps")
st.header(":blue[Markdown Examples]")
st.markdown("# This is a Main Page")
st.markdown("## Let's check Streamlit capabilities!")
st.markdown("> Here we can **insert** comments")
st.write(st.__version__)

