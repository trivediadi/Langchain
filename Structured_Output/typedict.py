from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

class review(TypedDict):
    summary: str
    sentiment:str

structured_model=model.with_structured_output(review)
result = structured_model.invoke(""" The hardware is great,but the software feels bloated. There are too many pre-installed apps that I never use. I wish I could remove them easily. Hoping for a software update that allows more customization.""")
print(result['summary'])
print(result['sentiment'])  # Output the sentiment of the review