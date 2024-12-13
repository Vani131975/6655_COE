import streamlit as st

st.header("Grade calculator")

project=st.number_input("give project score ",min_value=1,step=1)
internal=st.number_input("give internal score ",min_value=1,step=1)
external=st.number_input("give external score ",min_value=1,step=1)

if st.button("CALCULATE"):
    if (project >= 50 and internal >= 50 and external >= 50):
        pro_sc = (project * 70) / 100
        int_score = (internal * 10) / 100
        ext_score = (external * 20) / 100
        total = pro_sc + int_score + ext_score
        if (total > 90):
            st.success(f"A grade [Total marks: {total}]")
        elif (total > 80 and total <= 90):
            st.success(f"B grade [Total marks: {total}]")
        else:
            st.success(f"C grade [Total marks: {total}]")
    else:
        if (internal < 50):
            st.error(f"student failed in internal, {internal} marks")
        if (external < 50):
            st.error(f"student failed in external, {external} marks")
        if (project < 50):
            st.error(f"student failed in project, {project} marks")
