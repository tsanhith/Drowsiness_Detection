import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

# Load the drowsiness detection model
model = load_model(r"C:\Users\Kalivemula Rajendra\Desktop\Project 1\Final\drowsiness_detection_model1.keras")  # Specify the path to your trained model file

# Labels for drowsy and not drowsy
labels = {0: "Not Drowsy", 1: "Drowsy"}

# Preprocess the image for model input
def preprocess_image(img):
    img = img.resize((75, 75))  # Resize image to match model input size
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Function to make prediction
def predict_drowsiness(img):
    img = preprocess_image(img)
    prediction = model.predict(img)
    return labels[np.argmax(prediction)]

# Dashboard
st.title("Drowsiness Detection")

upload = st.file_uploader(label="Upload Image Here:", type=["png", "jpg", "jpeg"])

if upload:
    img = Image.open(upload)

    prediction = predict_drowsiness(img)

    fig = plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.axis('off')
    plt.title(prediction)
    st.pyplot(fig, use_container_width=True)
