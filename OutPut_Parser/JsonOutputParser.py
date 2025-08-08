from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser= JsonOutputParser()
template=PromptTemplate(
    template="Give me the name,age and city of a cartoon character Ben10. \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
prompt=template.format()
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)