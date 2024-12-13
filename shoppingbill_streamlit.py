import streamlit as st

st.header("Shopping bill calculation")
basic=st.number_input("enter basic salary",min_value=1,step=1)
s1=st.number_input("enter 1st shopping bill",min_value=1,step=1)
s2=st.number_input("enter 2nd shopping bill",min_value=1,step=1)
s3=st.number_input("enter 3rd shopping bill",min_value=1,step=1)

total=s1+s2+s3
spent=(total/basic)*100

if st.button("Total amount spent"):
    st.subheader("total bill is")
    st.success(total)
if st.button("percentage in my salary"):
    st.subheader("the percentage of amount spent is")
    st.success(spent)
