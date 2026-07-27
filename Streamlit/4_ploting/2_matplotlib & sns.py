import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Loading the dataframe
df = pd.read_csv('Images/iris.csv')
st.subheader("Data visualization with seaborn & Matplotlib")

######### 1. Displaying the DataFrame #########
st.text("1. Displaying the dataframe")
st.dataframe(df)

######### 2. Displaying the graph using matplotlib #########
st.text("2. bar plot using matplotlib")
Bar_count_PLOT = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(Bar_count_PLOT)

######### 3. Displaying the graph using seaborn #########
st.text("3. histplot using seaborn")
Dist_plot = plt.figure(figsize=(15,8))
sns.histplot(df['sepal_length'], kde=True)
st.pyplot(Dist_plot)

######### 4. Displaying the multiple graph #########
st.text("4. display multiple graphs")
col1, col2 = st.columns(2)
with col1:
    col1.write('KDE - False')
    fig1 = plt.figure()
    sns.histplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.write('HIST - False')
    fig2 = plt.figure()
    sns.kdeplot(df['sepal_length'])
    st.pyplot(fig2)

######### 5. Changing the style of graph #########
st.text('5. Changing the style of graph')
col1, col2 = st.columns(2)
with col1:
#    col1.write('KDE - False')
    KDE_False = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.kdeplot(df['petal_length'])
    st.pyplot(KDE_False)
with col2:
#   col2.write('HIST - False')
    HIST_False = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.kdeplot(df['petal_length'])
    st.pyplot(HIST_False)

######### 6. Scatter plot #########
st.text('6. Scatter plot')
scatter_PLOT, ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,500)))
st.pyplot(scatter_PLOT)

######### 7. Count plot #########
st.text('7. Count plot')
count_PLOT = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(count_PLOT)

######### 8. Box plot #########
st.text('7. Box plot')
Box_PLOT = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(Box_PLOT)

######### 9. Violin plot #########
st.text('7. Violin plot')
Violin_PLOT = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(Violin_PLOT)