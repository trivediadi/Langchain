from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
   template= """ Please summarize the research paper '{paper_input}' in {style_input} style with {length_input} length.
    1.Mathematical Explaination
       -include mathematical notations and equations in the paper
       -Explain the mathematical concepts in a clear and concise manner
    2.Analogies
       -Use relatable analogies to explain complex concepts
    If certain information is not available in the paper, please respond "insufficient informations" instead of gussing.
    Ensure that the summary is comprehensive and covers all key aspects of the paper and in given length."""
    ,input_variables=['paper_input','style_input','length_input']
)
template.save('template.json')  