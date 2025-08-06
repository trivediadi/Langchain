from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{user_input}')
])
# load chat history
chat_history = []
with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())
print(chat_history)
# create prompt
prompts=chat_template.invoke({
    'chat_history': chat_history,
    'user_input': 'I want to request a refund for my order #12345'
})
print(prompts)