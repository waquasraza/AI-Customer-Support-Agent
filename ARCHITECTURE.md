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
                    ┌─────────────────────┐
                    │    Router Agent     │
                    └──────────┬──────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │                       │                       │
       ▼                       ▼                       ▼

┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Billing Agent│      │Account Agent │      │Technical Agent│
└──────┬───────┘      └──────┬───────┘      └──────┬───────┘
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             │
                             ▼
                    ┌─────────────────────┐
                    │     Retriever       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      ChromaDB       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      OpenAI LLM     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Support Answer    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │ Answer Found ?      │
                    └──────┬───────┬──────┘
                           │       │
                         YES       NO
                           │       │
                           ▼       ▼

                   Return Answer  Escalation Agent
                                      │
                                      ▼
                               SQLite Tickets
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
ChromaDB
```

---

## Conversation Memory Flow

```text
Customer Message
      │
      ▼
SQLite Messages Table
      │
      ▼
Conversation History
      │
      ▼
Prompt Construction
      │
      ▼
OpenAI GPT
```

---

## Ticket Escalation Flow

```text
Customer Question
        │
        ▼
AI Response Generation
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
         SQLite Storage
```

---

## Database Schema

### Tickets

```sql
ticket_id
category
question
status
created_at
```

### Conversations

```sql
session_id
```

### Messages

```sql
session_id
role
content
created_at
```