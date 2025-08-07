from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

class review(BaseModel):
    key_themes: list[str]=Field(description="Key themes of the review")
    summary: str=Field(description="Summary of the review")
    sentiment: str=Field(description="Sentiment of the review (positive, negative, neutral)")

structured_model=model.with_structured_output(review)
result = structured_model.invoke(""" The hardware is great,but the software feels bloated. There are too many pre-installed apps that I never use. I wish I could remove them easily. Hoping for a software update that allows more customization.""")
print(result.summary)
print(result.sentiment)
print(result.key_themes)  # Output the key themes of the review