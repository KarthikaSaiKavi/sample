import streamlit as st

st.title("Result Checker")

marks = st.number_input("Enter marks")

if marks >= 50:
    st.success("Pass ✔")
else:
    st.error("Fail ❌")
