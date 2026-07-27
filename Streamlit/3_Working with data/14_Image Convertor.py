import streamlit as st
from PIL import Image

def Convert_image(uploaded_image, new_format):
    with Image.open(uploaded_image) as img:
        new_name = uploaded_image.name.split('.')[0] + '.' + new_format
        final_path = 'Images/' + new_name
        img = img.convert('RGB')
        img.save(final_path)
        st.success('Your converted image is saved at "' + final_path + '"')

st.title("Image Convertor")

image_file = st.file_uploader("Upload your image ",
                              type = ['png','jpeg', 'jpg'])

new_format = st.selectbox("Select the output format",
            options = ("png", "jpeg", "jpg"),
            help = "Choose one"
        )

if st.button("Convert"):
    if image_file is not None:
        Convert_image(image_file, new_format)
    else:
        st.error("Please upload the image file")
