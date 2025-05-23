from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os
from dotenv import load_dotenv
load_dotenv()

docs = []
with open("data/cleaned_docs.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)
        docs.append(Document(page_content=entry["page_content"], metadata=entry["metadata"]))

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = FAISS.from_documents(split_docs, embedding)

vectorstore.save_local("vector_store_poker")
print("✅ Vector store created at vector_store_poker/")
