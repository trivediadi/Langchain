from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser = StrOutputParser()

prompt= PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)
prompts2 = PromptTemplate(
    template="Give a small explaination on this  {joke}",
    input_variables=["joke"]
)
chain= RunnableSequence(
    prompt | model | parser | prompts2 | model | parser
)

result = chain.invoke({"topic": "cats"})
print(result)