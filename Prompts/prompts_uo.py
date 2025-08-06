from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.0)
st.header("Research Tool")

user_input=st.text_input("Enter your prompt")

if st.button('SUBMIT'):
    result=model.invoke(user_input)
    st.write(result.content)