import streamlit as st
import numpy as np 
import time

#Static columns Creation
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Cat",text_alignment = "center")
    st.image("Images/CAT.jpeg", caption = "This is an cat")
with col2:
    st.header("Dog",text_alignment = "center")
    st.image("Images/dog.jpeg", caption = 'This is Dog')
with col3:
    st.header("Owl",text_alignment = "center")
    st.image("Images/OWL.jpeg", caption = 'this is an OWL')

#For dynamic columns
n = st.number_input("How many columns do you want?", min_value = 1)

cols = st.columns(n)

for i in cols:
    with i:
        st.image("Images/CAT.jpeg")
