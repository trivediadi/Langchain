from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
prompts=PromptTemplate(
    template="Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)
parser= StrOutputParser()

chain = prompts | model | parser
result = chain.invoke({"topic": "Black Holes"})
print(result)  
chain.get_graph().print_ascii()