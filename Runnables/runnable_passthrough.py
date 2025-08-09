from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a joke about this  {topic}",
    input_variables=["topic"]
    )
prompt2 = PromptTemplate(
    template="Generate a 5 line explaination based on this joke  {topic}",
    input_variables=["topic"]
)

joke_chain = RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(
        prompt2 | model | parser
    )
}
)
chain=RunnableSequence(
    joke_chain,parallel_chain
)
result = chain.invoke({"topic": "cats"})
print(result)
