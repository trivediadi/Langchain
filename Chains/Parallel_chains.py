from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model1 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash")
model2 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

prompts1 = PromptTemplate(
    template="Generate a short and simple notes from the following text {text}.",
    input_variables=["text"]
)
prompts2 = PromptTemplate(
    template="Write a 5 short questions from the following text. /n {text}?",
    input_variables=["text"]
)
prompts3= PromptTemplate(
    template="Merge the provided notes and quiz into single document. /n notes->{notes} and quiz->{quiz}",
    input_variables=["notes", "quiz"]
)
parser = StrOutputParser()

Parallel_chain = RunnableParallel(
    {
        "notes": prompts1 | model1 | parser,
        "quiz": prompts2 | model2 | parser
    }
)
merge_chain = prompts3 | model1 | parser
chain=Parallel_chain | merge_chain
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.


"""
result = chain.invoke({"text": text})
print(result)

chain.get_graph().print_ascii()