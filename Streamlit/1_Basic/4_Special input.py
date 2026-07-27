import streamlit as st

st.subheader("1. Radio buttom")
gender = st.radio("Select you gender:",
                  options = ('Male','Female','Others'),
                  help = "Choose one",
                  horizontal = True
                  )
st.write("you've selected: ",gender)

st.subheader("2. Select box")
option = st.selectbox("Select your option",
                      options = ("Data Science", "Machine Learning", "Analysis"),
                      help = "Choose one"
             )
st.write("you've selected: ",option)

st.subheader("3. Multi-select box")
options = multiselect = st.multiselect("Select you option",
                      options = ("Data Science", "Machine Learning", "Analysis"),
                      help = "Choose one",
                      default = "Data Science"
)

st.subheader("4. button")
if st.button("Say hello"):
    st.write("Hey everyone!")

st.subheader("5. Check box")
if st.checkbox("I agree to the terms and conditions", help = "You must agree to proceed"):
    st.write("Thanks for agreering")

st.subheader("6. Colour picker")
colour = st.color_picker("Select your favourite colour: ")
st.write("You've selected: ",colour, "Colour")

st.button("Summit your responce")