import os
import time

from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in your .env file")


def load_document(docs_path="docs"):
    print(f"\nLoading files from {docs_path}...")

    if not os.path.exists(docs_path):
        raise FileNotFoundError(
            f"Directory {docs_path} doesn't exist."
        )

    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader,
    )

    documents = loader.load()

    if not documents:
        raise FileNotFoundError(
            f"No .txt files found in {docs_path}."
        )

    print(f"Loaded {len(documents)} documents.")

    return documents


def split_documents(
    documents,
    chunk_size=1500,
    chunk_overlap=150,
):
    print("\nSplitting documents into chunks....")

    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks


def create_vector_store(
    chunks,
    persist_directory="db/chroma_db",
):
    print("\nCreating embeddings and storing them in ChromaDB...")

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        api_key=API_KEY,
    )

    print("Creating vector store...")

    # Create an empty Chroma collection first
    vector_store = Chroma(
        collection_name="rag_documents",
        embedding_function=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={
            "hnsw:space": "cosine"
        },
    )

    # Process documents in batches
    batch_size = 20

    total_chunks = len(chunks)

    for start in range(0, total_chunks, batch_size):

        end = min(start + batch_size, total_chunks)

        batch = chunks[start:end]

        print(
            f"Embedding chunks {start + 1}-{end} "
            f"of {total_chunks}..."
        )

        while True:

            try:

                vector_store.add_documents(batch)

                print(
                    f"Successfully added {len(batch)} chunks."
                )

                break

            except Exception as e:

                error_message = str(e)

                if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:

                    print(
                        "Rate limit reached. "
                        "Waiting 35 seconds before retrying..."
                    )

                    time.sleep(35)

                else:
                    raise

        # Small delay between batches
        time.sleep(2)

    print(
        f"\nFinished creating vector store."
        f"\nStored at: {persist_directory}"
    )

    return vector_store


def main():

    print("Starting ingestion pipeline...")

    documents = load_document("docs")

    chunks = split_documents(
        documents=documents,
        chunk_size=1500,
        chunk_overlap=150,
    )

    create_vector_store(
        chunks=chunks,
        persist_directory="db/chroma_db",
    )

    print("\nIngestion pipeline completed successfully!")


if __name__ == "__main__":
    main()