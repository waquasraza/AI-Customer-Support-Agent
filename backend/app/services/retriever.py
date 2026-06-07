from langchain_chroma import Chroma

from app.services.embeddings import get_embeddings


def get_relevant_documents(question: str):

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(question)

    return docs