import streamlit as st

st.title("Even or Odd")
num1=st.number_input("Enter any number",min_value=1,step=1)
if st.button("Even/Odd"):
    if num1%2==0:
        st.success("Even Number")
    else:
        st.success("Odd Number")