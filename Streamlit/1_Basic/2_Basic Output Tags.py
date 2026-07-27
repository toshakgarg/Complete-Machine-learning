import streamlit as st

#Title
st.title("Title: Toshak")

#Header
st.header("Header: Toshak")

#Subheader
st.subheader("Subheader: Toshak")

#Text
st.text("Text: Toshak")

#Markdown
st.markdown("Markdown: This is a markdown text.")       #P tag
st.markdown("# H1")           #h1
st.markdown("## H2")          #h2
st.markdown("### H3")         #h3
st.markdown("#### H4")        #h4
st.markdown("##### H5")       #h5
st.markdown("###### H6")      #h6

#Formatting
st.markdown("**Bold**")         #Bold
st.markdown("*Italic*")           #Italic
st.markdown("***Bold + Italic***")         #Bold + Italic
st.markdown("~~Strikethrough~~")         #Strikethough

#Ordered List
st.markdown("1. Item 1")         #Ordered List
st.markdown("2. Item 2")         #Ordered List
st.markdown("3. Item 3")         #Ordered List

#Unordered list
st.markdown("- Item 1")         #Unordered List
st.markdown("- Item 2")         #Unordered List
st.markdown("- Item 3")         #Unordered List

st.markdown(''' 1. item1  
            2. item2''')

# Writie function
st.write("this is a text.")
st.write(range(10,20))          #Write can write any code too.
