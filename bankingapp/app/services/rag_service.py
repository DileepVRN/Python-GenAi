from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Sample banking data (replace later with DB data)
documents = [
    "User spent ₹5000 on Amazon",
    "User transferred ₹20000 to savings account",
    "Electricity bill payment ₹3000",
    "Salary credited ₹80000",
]

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create vector DB
vector_store = FAISS.from_texts(documents, embeddings)

def search_transactions(query: str):
    results = vector_store.similarity_search(query, k=3)
    return [doc.page_content for doc in results]

from app.services.llm_service import ask_llm

def rag_chat(query: str):
    context = search_transactions(query)

    prompt = f"""
    You are a banking assistant.

    Context:
    {context}

    Question:
    {query}
    """

    return ask_llm(prompt)