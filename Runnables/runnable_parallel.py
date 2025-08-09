from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser = StrOutputParser()
model1 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash")
prompt1 = PromptTemplate(
    template="Generate a tweet about this  {topic}",
    input_variables=["topic"])
prompt2 = PromptTemplate(
    template="Generate a linkedin post about this  {topic}",
    input_variables=["topic"]
    )
parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1 , model , parser),
        "linkedin_post": RunnableSequence(
            prompt2, model1, parser
        )
    }
)
result = parallel_chain.invoke({"topic": "AI and its impact on society"})
print(result['tweet'])
print('/n')
print(result['linkedin_post'])