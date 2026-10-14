import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=os.getenv("GEMINI_API_KEY"),
)

texts = [
    "This is test document one.",
    "This is test document two.",
    "This is test document three.",
    "This is test document four.",
    "This is test document five.",
]

print(f"Embedding {len(texts)} texts...")

results = embeddings.embed_documents(texts)

print(f"Successfully created {len(results)} embeddings.")
print(f"Embedding dimensions: {len(results[0])}")