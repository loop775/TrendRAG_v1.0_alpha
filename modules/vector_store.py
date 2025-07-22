from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from embedding_generator import get_embeddings

def setup_vector_store(trends):
    docs = [Document(page_content=trend) for trend in trends]
    embeddings = [get_embeddings(trend) for trend in trends]
    return FAISS.from_embeddings(embeddings, docs)

def query_similar(vector_store, query_embedding, k=5):
    return vector_store.similarity_search_by_vector(query_embedding, k=k)