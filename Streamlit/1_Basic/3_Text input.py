import streamlit as st
from datetime import datetime as dt

#Text input
st.subheader("1. Text input")
name = st.text_input("Enter your name", value ="Name")
st.write(f"Hello,", name)

#Password
st.subheader("2. Password input:")
password = st.text_input("Enterr your password:", 
                         type="password", 
                         help = "Atlest have 8 charactor.")

#Text ares
st.subheader("3. Text area") # In order to take larger input, we can use text area
message = st.text_area("Tell me something about yourself (500 char)", 
                       height=200,    #To change the height of text box
                       max_chars=500, #Fix the maximun charactor to 500
                       help = "Max 500 characters allowed")

#Numeric input
st.subheader("4. Password input:")
st.number_input("Enter your age: ", 
                min_value = 0,
                max_value = 110,
                step=1)

# Datetime input
today = dt.now().date()
st.subheader("5. Date input:")
date = st.date_input("Enter the date: ", 
              value = today, 
              min_value = today,
              max_value = today.replace(year = today.year + 1)
              )
st.write("You have selected date: ", dt.strftime(date, '%m/%d/%Y'))