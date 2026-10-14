import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
)

response = llm.invoke("Explain what RAG is in two sentences.")

print(response.content)
