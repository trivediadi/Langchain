from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.0)
st.header("Research Tool")

paper_input=st.selectbox("Select Research Paper Name",["Select...","Attention is all you need","Bert: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT-3: Language Models are Few-Shot Learners","T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"])
style_input=st.selectbox("Select Style",["Select...","Formal","Informal","Technical","Conversational"])
length_input=st.selectbox("Select Length",["Select...","Short(1-2 paragraph)","Medium(3-5 paragraph)","Long(detaled explaination)"])

# templete
template=PromptTemplate(
   template= """ Please summarize the research paper '{paper_input}' in {style_input} style with {length_input} length.
    1.Mathematical Explaination
       -include mathematical notations and equations in the paper
       -Explain the mathematical concepts in a clear and concise manner
    2.Analogies
       -Use relatable analogies to explain complex concepts
    If certain information is not available in the paper, please respond "insufficient informations" instead of gussing.
    Ensure that the summary is comprehensive and covers all key aspects of the paper and in given length."""
    ,input_variables=['paper_input','style_input','length_input']
)
prompt=template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})
if st.button('SUBMIT'):
    result=model.invoke(prompt)
    st.write(result.content)
