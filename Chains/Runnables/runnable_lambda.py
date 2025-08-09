from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel,RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
def word_count(text) :
    """Count the number of words in a text."""
    return len(text.split())
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a joke about this  {topic}",
    input_variables=["topic"]   
)

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
    # 'word_count': RunnableLambda(lambda x:len(x.split()))
})
chain= RunnableSequence(
    joke_chain, parallel_chain
)

result = chain.invoke({"topic": "cats"})
print(result['word_count'])
