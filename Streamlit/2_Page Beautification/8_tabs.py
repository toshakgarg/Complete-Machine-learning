import streamlit as st
import numpy as np 
import pandas as pd
import time

#Static
tab1, tab2, tab3 = st.tabs(["Cat", "Dog","OWL"],)
tab1.image("Images/CAT.jpeg")
tab2.image("Images/Dog.jpeg")
tab3.image("Images/OWL.jpeg")

#Dynamic
images = pd.read_csv("Images/imgs.csv")                            # Importing CSV file
images['tags'] = list(images['tags'].str.split(", ").str[0])       # rewrite tags columns

n = st.number_input("Enter numbers of image tabs",                 # User enter number of tabs they want
                    min_value =1,                                  # minimum values = 1 
                    max_value = 20)                                # maximum values = 10

random_images = images.sample(n)                                   # Choosing random n images

tab = st.tabs(list(random_images["tags"]))                         # passing the list of random images's tabs as tab name
y=0
for i in tab:
    i.image(list(random_images['img_link'])[y])
    y=y+1