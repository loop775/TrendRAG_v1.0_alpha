from langchain.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

def get_embeddings(text):
    return embedding_model.embed_query(text)