# Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import os

## Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.environ["OPEN_API_KEY"], model_name="text-davinci-003", temperature=0.5)
    response = llm(question)
    return response

## Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# User input
input_question = st.text_input("Input: ", key="input")

# Ask button
submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    # Get the response only if the button is clicked
    response = get_openai_response(input_question)
    st.subheader("The Response is")
    st.write(response)
