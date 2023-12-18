import streamlit as st
st.set_page_config(page_title="MLOps",
                   page_icon=None,
                   layout= "centered",
                   initial_sidebar_state="auto",
                   menu_items=None
)

st.title("Streamlit: MLOps")
st.header(":green[Button Examples]")

widget = st.radio("Which widget do you prefer?", ["Button", "Checkbox"])

st.write("Here's your widget:")

if widget == "Button":
    algorithms_list_1 = ["Random Forest", "Support Vector Machine", "Multilayer Perception"]
    algorithms_list_2 = ["Decision Tree", "KNN"]

    if st.button("Algorithms 1", type="primary"):
        st.write(algorithms_list_1)

    if st.button("Algorithms 2", type="secondary"):
        st.write(algorithms_list_2)

if widget == "Checkbox":
    if st.checkbox("Accept action"):
        st.write("Thanks for accepting!")
    else:
        st.write("Please accept me!")

