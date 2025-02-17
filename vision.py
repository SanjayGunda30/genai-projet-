from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("Google_API_KEY"))
model = genai.GenerativeModel("gemini-1.0")

# function to generate text and text using google AI
def get_gemini_responce(input_text, image):
    if input_text and image:
        combined_input = f"{input_text} [Image: {image}]"
        response = model.generate_content(combined_input)
    elif input_text:
        response = model.generate_content(input_text)
    else:
        response = model.generate_content(image)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="Gemini image")
st.header("Gemini LLm application")
input_text = st.text_input("Input:  ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Ask the Question about the image")

# when the submit button is clicked
if submit:
   response = get_gemini_responce(input_text, image)
   st.subheader("Response:")
   st.write(response)

