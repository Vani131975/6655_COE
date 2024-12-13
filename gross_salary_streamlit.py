import streamlit as st
st.header("GROSS SALARY CALCULATION")
a=st.number_input("enter basic salary ",min_value=1,step=1)
if(a<=10000 and a>1000):
    hra=(a*67)/100
    da = (a * 73) / 100
elif(a>=20000):
    hra = (a*73)/100
    da = (a * 89)/100
else:
    hra = (a * 69)/ 100
    da = (a * 76)/ 100
gross=hra+da+a
if st.button("gross salary"):
    st.info(f"basic salary {a}")
    st.info(f"HRA {hra}")
    st.info(f"DA {da}")
    st.success(f"Gross salary is {gross}")
