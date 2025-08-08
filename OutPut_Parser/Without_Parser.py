from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#1st prompt
template1=PromptTemplate(
    template="Write a detailed report on topic {topic}?",
    input_variables=["topic"]
)

#2nd prompt
template2=PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}?",
    input_variables=["text"]
)

prompt1=template1.format(topic="Black Holes")
result1=model.invoke(prompt1)
prompt2=template2.format(text=result1.content)
result2=model.invoke(prompt2)

print(result2.content)