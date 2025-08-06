from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.0)
st.header("Research Tool")

paper_input=st.selectbox("Select Research Paper Name",["Select...","Attention is all you need","Bert: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT-3: Language Models are Few-Shot Learners","T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"])
style_input=st.selectbox("Select Style",["Select...","Formal","Informal","Technical","Conversational"])
length_input=st.selectbox("Select Length",["Select...","Short(1-2 paragraph)","Medium(3-5 paragraph)","Long(detaled explaination)"])

templete=load_prompt('template.json')


if st.button('SUBMIT'):
    chain= templete | model
    result=chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
   })
    st.write(result.content)
