import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['L1','L2','L3'])

# Ploting line chart
st.title("1. Line Chart")
st.line_chart(chart_data)

# Ploting area chart
st.title("2. Area chart")
st.area_chart(chart_data)

# Ploting bar graph
st.title("3. Bar chart")
st.bar_chart(chart_data)