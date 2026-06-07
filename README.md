# AI Customer Support Agent

An AI-powered Customer Support Platform built using FastAPI, LangChain, LangGraph, OpenAI, ChromaDB, and SQLite.

## Overview

This project simulates a production-grade customer support system that combines Retrieval-Augmented Generation (RAG), multi-agent workflows, conversation memory, and automated ticket escalation.

The platform allows customers to ask questions about company policies, pricing plans, account management, and technical integrations. Questions are automatically routed to specialized AI agents and answered using information stored in the company's knowledge base.

The entire workflow is orchestrated using LangGraph, enabling stateful agent execution, memory management, routing, escalation, and response generation.

When the system cannot confidently answer a question, it automatically creates a support ticket for human review.

---

## Features

### Knowledge Base Management

* Upload company PDF documents
* Automatic document chunking
* OpenAI embeddings generation
* ChromaDB vector storage

### Retrieval-Augmented Generation (RAG)

* Semantic search over company documents
* Context-aware AI responses
* Hallucination reduction through knowledge retrieval

### Multi-Agent Architecture

* Router Agent
* Billing Agent
* Technical Support Agent
* Account Support Agent
* Escalation Agent

### LangGraph Workflow

* Stateful workflow execution
* Conditional routing between agents
* Memory loading and persistence
* Automated escalation workflow

Workflow:

Load Memory → Router → Specialized Agent → Escalation Check → Save Memory → Response

### Conversation Memory

* Session-based chat history
* Persistent conversation storage using SQLite
* Context-aware follow-up questions
* Multi-turn conversation support

### Ticket Escalation System

* Automatic escalation when answers are unavailable
* Ticket creation and tracking
* Ticket status management APIs
* Persistent ticket storage

### Persistent Storage

* SQLite ticket storage
* SQLite conversation history
* SQLite message history
* Session management

---

## Tech Stack

### Backend

* FastAPI
* Python

### AI & LLM

* OpenAI GPT-4o Mini
* LangChain
* LangGraph

### Vector Database

* ChromaDB

### Database

* SQLite

### Embeddings

* OpenAI Embeddings (text-embedding-3-small)

---

## Architecture

Customer Question

↓

Load Memory Node

↓

Router Agent

↓

Billing Agent / Technical Agent / Account Agent

↓

Escalation Check

↓

Save Memory Node

↓

Response

---

## API Endpoints

### Knowledge Base

POST /knowledge/upload

Upload PDF documents to the knowledge base.

### Chat

POST /chat

Ask questions and receive AI-generated responses.

### Tickets

GET /tickets

Retrieve all support tickets.

GET /tickets/{ticket_id}

Retrieve a specific ticket.

PATCH /tickets/{ticket_id}

Update ticket status.

---

## Example Questions

### Billing

* What is your cheapest plan?
* How much does the Professional plan cost?
* Can I get a refund?

### Technical

* Do you provide API access?
* Can I integrate your platform with my application?
* What integrations are supported?

### Account

* How do I reset my password?
* My account is locked.
* How can I update my profile settings?