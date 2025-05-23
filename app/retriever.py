import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

load_dotenv()

def load_vectorstore():
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    return FAISS.load_local("vector_store_poker", embedding, allow_dangerous_deserialization=True)

vectorstore = load_vectorstore()

def retrieve_context(query: str, k: int = 5) -> str:
    results = vectorstore.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in results])
    return context
