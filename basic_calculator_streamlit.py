import streamlit as st

st.header("basic calculations")
num1=st.number_input("Enter number 1",min_value=1,step=1)
num2=st.number_input("Enter number 2",min_value=1,step=1)

add = num1 + num2
sub=num1-num2
mul=num1*num2
div=num1/num2

if st.button("ADD"):
    st.success(add)
if st.button("SUBTRACT"):
    st.success(sub)
if st.button("MULTIPLY"):
    st.success(mul)
if st.button("DIVIDE"):
    st.success(div)
