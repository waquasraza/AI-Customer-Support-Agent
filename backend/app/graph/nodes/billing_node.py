from app.services.agents.billing_agent import handle_billing_query

def billing_node(state):

    state["answer"] = handle_billing_query(
        state["question"],
        state["history_text"]
    )

    return state