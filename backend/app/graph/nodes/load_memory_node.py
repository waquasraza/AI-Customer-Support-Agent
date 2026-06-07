from app.services.conversation_service import get_conversation_history


def load_memory_node(state):

    history = get_conversation_history(
        state["session_id"]
    )

    state["history_text"] = history

    return state