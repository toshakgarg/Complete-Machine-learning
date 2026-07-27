import streamlit as st
import numpy as np 
import pandas as pd
import time

# Creating sample space
case = []
for i in range(100):
    case.append(np.random.randint(1,7))

# Creating list
dataframe = []
for i in range(1,7):
    dataframe.append({
        'number' : i,
        'count' : case.count(i)
        })

# Converting list to dataframe
df = pd.DataFrame(dataframe).set_index('number')

st.subheader("Frequency of getting face")
st.bar_chart(df)

####**********Expender & Empty**********####
# Expender                                  an expander widget that users can click to reveal an explanation.
with st.expander("See explaination: "):
    st.write("The charts shows the numbers i got from a rolling a diece 100 times and its basically about how many time each faces appears.")
    st.image("Images/dice.jpeg")

# Empty                                     function to create an empty element To reerite the whole thing (update the countdown)
with st.empty():
    st.write('You need to wait for 10 seconds')
    for seconds in range(11):
        st.write('⏳ ' + str(seconds) + ' seconds remained')
        time.sleep(1)
    st.write('10 seconds completed')

