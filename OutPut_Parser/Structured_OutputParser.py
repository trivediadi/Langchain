from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name="name", description="Name of the character"),
    ResponseSchema(name="age", description="Age of the character"),
    ResponseSchema(name="city", description="City where the character lives"),
    ResponseSchema(name="Family", description="Family members of the character just names")
]
parser= StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template="Give me the name,age and city of a cartoon character Ben10. \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
chain= template | model | parser
result=chain.invoke({})

print(result)