from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents=[
    "Virat Kohli is a famous cricketer.",
    "Sachin Tendulkar is a legendary cricketer.",
    "Lionel Messi is a world-renowned footballer.",
    "Cristiano Ronaldo is a top football player."
]
query="Tell me about legendary cricketers."
query_embedding = embeddings.embed_query(query)
document_embeddings = embeddings.embed_documents(documents)
scores = cosine_similarity([query_embedding], document_embeddings)[0]
index,score=sorted(list(enumerate(scores)),key=lambda x: x[1])[-1]
print(documents[index],score)  # Output the most similar document and its score