import streamlit as st
import numpy as np 
import pandas as pd
import time

#Page settings
st.set_page_config(page_title = "Dice frequency chart",
                   page_icon = "😎",
                   #layout = "wide"
                   )

####**********Expender & Empty**********####
# Expender                                  an expander widget that users can click to reveal an explanation.
with st.expander("See explaination: "):
    st.write("The charts shows the numbers i got from a rolling a diece 100 times and its basically about how many time each faces appears.")
    st.image("Images/dice.jpeg")


###********************###
# Spinner
with st.spinner("Wait for it"):
    time.sleep(5)
    st.write("Thanks for being patient")

# Progress bar with empty
with st.empty():
    for percentage_completed in range(100):
        time.sleep(0.1)
        st.progress(percentage_completed +1, text = "processing")
    st.success("Completed!")

# balloons & Snows
st.balloons()
st.snow()