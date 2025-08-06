from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

messages=[
    SystemMessage(content='You are a helful assistant.'),
    HumanMessage(content='Tell me about Langchain')
]
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages) 