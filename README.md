# AI Customer Support Agent

An AI-powered Customer Support Platform built using FastAPI, LangChain, OpenAI, ChromaDB, and SQLite.

## Overview

This project simulates a production-grade customer support system that combines Retrieval-Augmented Generation (RAG), multi-agent routing, conversation memory, and automated ticket escalation.

The platform allows customers to ask questions about company policies, pricing plans, account management, and technical integrations. Questions are automatically routed to specialized AI agents and answered using information stored in the company's knowledge base.

When the system cannot confidently answer a question, it automatically creates a support ticket for human review.

---

## Features

### Knowledge Base Management

* Upload company PDF documents
* Automatic document chunking
* Vector embeddings generation
* ChromaDB vector storage

### Retrieval-Augmented Generation (RAG)

* Semantic search over company documents
* Context-aware AI responses
* Hallucination reduction through knowledge retrieval

### Multi-Agent Architecture

* Billing Agent
* Technical Support Agent
* Account Support Agent
* Router Agent

### Conversation Memory

* Session-based chat history
* Persistent conversation storage using SQLite
* Context-aware follow-up questions

### Ticket Escalation System

* Automatic escalation when answers are unavailable
* Ticket creation and tracking
* Ticket status management APIs

### Persistent Storage

* SQLite ticket storage
* SQLite conversation history
* Session management

---

## Tech Stack

### Backend

* FastAPI
* Python

### AI & LLM

* OpenAI GPT-4o Mini
* LangChain

### Vector Database

* ChromaDB

### Database

* SQLite

### Embeddings

* OpenAI Embeddings (text-embedding-3-small)

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

Billing:

* What is your cheapest plan?
* How much does the Professional plan cost?

Technical:

* Do you provide API access?
* Can I integrate your platform with my application?

Account:

* How do I reset my password?
* My account is locked.