from langchain_openai import ChatOpenAI

from app.core.config import OPENAI_API_KEY


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)


def generate_support_answer(question, docs, history):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are a professional customer support assistant.

    Answer ONLY using the information
    provided in the company knowledge base.

    If information is not available,
    respond with:

    "I could not find that information in the knowledge base."

    Previous Conversation:

    {history}

    Knowledge Base:
    {context}

    Customer Question:
    {question}

    Provide a clear customer-friendly answer.
    """

    response = llm.invoke(prompt)

    return response.content