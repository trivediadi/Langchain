from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

while True:
    user_input=input('You: ')
    if user_input == 'exit':
        break
    else:
        result=model.invoke(user_input)
        print(f"Chatbot: {result.content}")