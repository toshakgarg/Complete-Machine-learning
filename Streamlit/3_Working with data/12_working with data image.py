import streamlit as st

# Image
st.subheader("Image from path")
st.image("Images/CAT.jpeg")

#Image from link
st.subheader("Image from link")
st.image("https://docs.streamlit.io/logo.svg", width = 200)

#Video from link
st.subheader("Video")
st.video("Images/VIDEO.mp4",
         start_time = 6         #To stat video from specific senond
        )

#Audio files
st.subheader("Audio")
st.audio("Images/AUDIO.mp3",
         start_time = 3         #To stat audio from specific senond
        )       