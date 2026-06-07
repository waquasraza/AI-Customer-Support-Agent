from fastapi import APIRouter, UploadFile, File

import os
import shutil

from app.services.document_loader import load_pdf
from app.services.chunker import chunk_documents
from app.services.vector_store import store_chunks

router = APIRouter(prefix="/knowledge", tags=["Knowledge Base"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save File
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Load PDF
    documents = load_pdf(file_path)

    # Chunk PDF
    chunks = chunk_documents(documents)

    # Add Metadata
    for chunk in chunks:
        chunk.metadata["source_file"] = file.filename

    # Store in ChromaDB
    store_chunks(chunks)

    return {
        "message": "Knowledge base updated",
        "file": file.filename,
        "pages": len(documents),
        "chunks": len(chunks),
        "stored_in_vector_db": True
    }