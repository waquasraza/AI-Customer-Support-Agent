from app.services.escalation_agent import escalate_issue


def escalation_node(state):

    answer = state["answer"]

    if "could not find" in answer.lower():

        ticket = escalate_issue(
            state["question"],
            state["agent_type"]
        )

        state["escalated"] = True
        state["ticket"] = ticket

    else:

        state["escalated"] = False
        state["ticket"] = None

    return state