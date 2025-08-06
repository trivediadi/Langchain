from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

chat_history = []
while True:
    user_input=input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    else:
        result=model.invoke(chat_history)
        chat_history.append(result.content)
        print(f"Chatbot: {result.content}")
print(chat_history)