from langchain_chroma import Chroma

from app.services.embeddings import get_embeddings


def store_chunks(chunks):

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    vector_store.add_documents(chunks)

    return vector_store