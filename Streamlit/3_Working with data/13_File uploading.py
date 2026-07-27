import streamlit as st
from PIL import Image
import pandas as pd

st.title("File uploading")

###############*****Image*****###############
st.subheader("1. Upload an image")
img_file = st.file_uploader("Upload your image",
                 type = ['png', 'jpeg', 'jpg']
                )
if img_file is not None:
    file_details = {'name' : img_file.name, 'Type' : img_file.type, 'size' : img_file.size}
    st.write(img_file)
    st.write(file_details)
    st.image(img_file)

###############*****Multiple Image*****###############
st.subheader("2. Upload multiple image")
img_file = st.file_uploader("Upload your image",
                 type = ['png', 'jpeg', 'jpg'],
                 accept_multiple_files = True
                )
if img_file is not None:
    st.image(img_file)


###############*****Audio*****###############
st.subheader("3. Upload an audio")
audio_file = st.file_uploader("Upload your audio",
                 type = ['wav', 'mp3']
                )
if audio_file is not None:
    file_details = {'name' : audio_file.name, 
                    'Type' : audio_file.type,
                    'size' : audio_file.size}
    #st.write(audio_file)
    st.write(file_details)
    st.audio(audio_file)


###############*****Video*****###############
st.subheader("4. Upload an video")
video_file = st.file_uploader("Upload your video",
                 type = ['mov', 'mp4'],
                 max_upload_size = 400
                )
if video_file is not None:
    file_details = {'name' : video_file.name, 
                    'Type' : video_file.type, 
                    'size' : video_file.size}
    #st.write(video_file)
    #st.write(file_details)
    st.video(video_file)


###############*****CSV*****###############
st.subheader("5. Upload an CSV")
CSV_file = st.file_uploader("Upload your CSV file",
                 type = ['csv'],
                 max_upload_size = 300
                )
if CSV_file is not None:
    file_details = {'name' : CSV_file.name, 
                    'Type' : CSV_file.type, 
                    'size' : CSV_file.size}
    #st.write(CSV_file)
    st.write(file_details)
    df = pd.read_csv(CSV_file)
    st.dataframe(df)

