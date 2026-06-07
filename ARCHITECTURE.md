# Architecture Diagram

## High-Level Architecture

```text
                          ┌─────────────────────┐
                          │      Customer       │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │     FastAPI API     │
                          └──────────┬──────────┘
                                     │
                                     ▼
                     ┌──────────────────────────────┐
                     │      LangGraph Workflow      │
                     └──────────────┬───────────────┘
                                    │
                                    ▼

                         ┌─────────────────────┐
                         │  Load Memory Node   │
                         └──────────┬──────────┘
                                    │
                                    ▼

                         ┌─────────────────────┐
                         │    Router Node      │
                         └──────────┬──────────┘
                                    │

           ┌────────────────────────┼────────────────────────┐
           │                        │                        │
           ▼                        ▼                        ▼

 ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
 │  Billing Agent  │    │  Account Agent  │    │ Technical Agent │
 └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                                 ▼

                     ┌─────────────────────┐
                     │ Escalation Node     │
                     └──────────┬──────────┘
                                │
                                ▼

                     ┌─────────────────────┐
                     │ Save Memory Node    │
                     └──────────┬──────────┘
                                │
                                ▼

                     ┌─────────────────────┐
                     │      Response       │
                     └─────────────────────┘
```

---

## LangGraph Workflow

```text
START
  │
  ▼
Load Memory
  │
  ▼
Router
  │
  ├── Billing Agent
  │
  ├── Technical Agent
  │
  └── Account Agent
  │
  ▼
Escalation Check
  │
  ▼
Save Memory
  │
  ▼
END
```

---

## Knowledge Base Pipeline

```text
PDF Upload
     │
     ▼
Document Loader
     │
     ▼
Text Chunking
     │
     ▼
OpenAI Embeddings
     │
     ▼
ChromaDB Vector Store
```

---

## Retrieval Pipeline (RAG)

```text
Customer Question
        │
        ▼
Retriever
        │
        ▼
Relevant Chunks
        │
        ▼
OpenAI GPT
        │
        ▼
Answer
```

---

## Conversation Memory Flow

```text
Customer Message
        │
        ▼
Load Memory Node
        │
        ▼
SQLite Messages
        │
        ▼
Conversation History
        │
        ▼
Prompt Construction
        │
        ▼
OpenAI GPT
        │
        ▼
Save Memory Node
        │
        ▼
SQLite Messages
```

---

## Ticket Escalation Flow

```text
Customer Question
        │
        ▼
Agent Response
        │
        ▼
Answer Available?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
   ▼         ▼
Respond   Create Ticket
              │
              ▼
         SQLite Tickets
```

---

## Database Schema

### tickets

```sql
ticket_id
category
question
status
created_at
```

### conversations

```sql
session_id
```

### messages

```sql
session_id
role
content
created_at
```

---

## Agent Responsibilities

### Router Agent

Classifies incoming questions into:

* billing
* technical
* account

### Billing Agent

Handles:

* pricing
* subscriptions
* invoices
* refunds

### Technical Agent

Handles:

* API questions
* integrations
* technical issues
* troubleshooting

### Account Agent

Handles:

* login issues
* password resets
* profile management
* account settings

### Escalation Agent

Handles:

* unanswered questions
* support ticket creation
* ticket persistence

```
```
