from langchain_huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv

load_dotenv()
embedding = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text="Delhi is the capital of India."
vector = embedding.embed_query(text)  # Example usage
print(str(vector))  # Output the embedding result
