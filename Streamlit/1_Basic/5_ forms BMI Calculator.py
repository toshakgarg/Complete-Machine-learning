import streamlit as st

st.title("BMI Calculator")

with st.form("BMI Calculator"):
    col1, col2, col3 = st.columns([3,2,1])

with col1:
    weight = st.number_input("Your weight in kg's")

with col2:
    Height = st.number_input("Your Height in meter", value = 1)

with col3:
    submit = st.form_submit_button("Calculate")

if submit:
    BMI = round((weight / ((Height*0.3048)**2)),2)
    st.write("Your BMI is: ", BMI)
    if (BMI <= 18.5):
        st.error("Underweight")
    elif(BMI>18.5 and BMI <=24.5):
        st.success("Healthy / Normal")
    elif(BMI>25 and BMI <=-29.9):
        st.warning("Overweight")
    elif(BMI>=30):
        st.error("Obese")

