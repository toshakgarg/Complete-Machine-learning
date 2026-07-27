import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np

def rotate_image(image, angle):
    img = np.array(image)
    height, width = img.shape[:2]
    M = cv.getRotationMatrix2D(center = (width/2, height/2),
                               angle = angle,
                               scale = 1                        # No scaling
                               )
    # Perform the rotation
    rotated_image = cv.warpAffine(img, M, (width, height))
    return rotated_image



st.title("image Rotator")
st.subheader("Upload an image")
img_file = st.file_uploader("upload your image", type = ['jpeg', 'png', 'jpg'])

st.subheader("Rotate image")
angle = st.slider("Choose the angle", min_value = -180, max_value = 180, value = 0, step = 1,)

if img_file is not None:
    image = Image.open(img_file)
    rotated_image = rotate_image(image, angle)
    st.image(rotated_image, width = 400)
else:
    st.warning("Please upload the image")
