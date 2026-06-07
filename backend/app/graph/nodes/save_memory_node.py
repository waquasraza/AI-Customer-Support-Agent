from app.services.conversation_service import save_message


def save_memory_node(state):

    save_message(
        state["session_id"],
        "user",
        state["question"]
    )

    save_message(
        state["session_id"],
        "assistant",
        state["answer"]
    )

    return state