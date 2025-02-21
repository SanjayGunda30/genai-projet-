from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("Google_API_KEY"))
MODEL = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Function to generate text using Google AI
def get_gemini_response(text, image):
    if text and image:
        response = MODEL.generate_content([text, image])
    elif text:
        response = MODEL.generate_content([text])
    else:
        response = MODEL.generate_content([image])
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="VisionText AI")
st.header("VisionText AI application")
text = st.text_input(" Your Question ", key="input")
uploaded_file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

submit = st.button("Submit")  # Button to submit the question
# When the submit button is clicked

if submit:
    response = get_gemini_response(text, image)
    st.subheader("Response:")
    st.write(response)  # Display the response

