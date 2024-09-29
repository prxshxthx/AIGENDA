import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCoiiV6gqjpPdzrdZBO-xhIYWnxRuID3kU")

model= genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data,prompt):
    response = model.generate_content([input_text,image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data= uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type" : uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file not uploaded")

st.set_page_config(page_title="WEI Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by IEEE WEI")
st.sidebar.write("Powered by google gemini AI")
st.header("RoboBill")
st.subheader("hey there! I'm RoboBill")
st.subheader("Manage your expenses with ")
input = st.text_input("What do you want to do?",key="input")
uploaded_file=st.file_uploader("choose an image from you gallery",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width= True)
ssubmit = st.button("Let's Go!")

input_prompt ="""you are an expert in reading inc=voices.
we are going to upload an image of an image and you will have to answer any tuple of question that the user asks you.
you have to greet the user first.make sure to keep the fonts uniform ans give the items list in point wise format .
ask the user to use it again"""

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data,input)
    st.write(response)
