from dotenv import load_dotenv
load_dotenv()
import os

import streamlit as st  
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_API_KEY"))

## Function to generate text Using google AI
model =  genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="Gemini")
st.header("Gemini LLm application")

input = st.text_input("Input:  ",key="input")
submit = st.button("Ask the Question")

# wenn the submit button is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("Response:")
    st.write(response)