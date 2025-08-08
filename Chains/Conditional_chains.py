from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Literal
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser= StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Sentiment of the feedback")
parser2= PydanticOutputParser(pydantic_object=Feedback)
prompts1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}.",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)
prompts2=PromptTemplate(
    template="Generate a appropriate response to the positive feedback: {feedback}.",
    input_variables=["feedback"]
)
prompts3=PromptTemplate(
    template="Generate a appropriate response to the negative feedback: {feedback}.",
    input_variables=["feedback"]
)
classifier_chain = prompts1 | model | parser2
branch_chain= RunnableBranch(
    (lambda x:x.sentiment=='positive',prompts2 | model | parser),
    (lambda x:x.sentiment=='negative',prompts3 | model | parser),
    RunnableLambda(lambda x: "could not classify sentiment")
)
chain= classifier_chain | branch_chain
result=chain.invoke({"feedback": "The phone is bad, I hate it!"})
print(result)