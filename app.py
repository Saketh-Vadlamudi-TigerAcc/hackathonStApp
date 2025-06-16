import streamlit as st

st.set_page_config(layout="wide")
st.title("Hello from Streamlit on Databricks!")
st.write("This is a basic Streamlit app deployed via Databricks Apps.")

name = st.text_input("What's your name?", "World")
st.write(f"Hello, {name}!")

if st.button("Click Me!"):
    st.write("You clicked the button!") 
