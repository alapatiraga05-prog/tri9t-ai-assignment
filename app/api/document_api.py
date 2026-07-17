from pathlib import Path
from typing import List

from fastapi import APIRouter, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document
from app.schemas.document_schema import DocumentRead
from app.services.ingest_service import IngestService

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/ingest", response_model=DocumentRead)
def ingest_document(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    upload_dir = Path("generated")
    upload_dir.mkdir(exist_ok=True)

    save_path = upload_dir / file.filename

    with save_path.open("wb") as handle:
        handle.write(file.file.read())

    db: Session = SessionLocal()

    try:
        latest_document = (
            db.query(Document)
            .filter(Document.name == file.filename)
            .order_by(Document.version.desc())
            .first()
        )

        version = 1 if latest_document is None else latest_document.version + 1

    finally:
        db.close()

    service = IngestService()

    service.ingest(
        pdf_path=str(save_path),
        document_name=file.filename,
        version=version,
    )

    db = SessionLocal()

    try:
        document = (
            db.query(Document)
            .filter(
                Document.name == file.filename,
                Document.version == version,
            )
            .first()
        )

        if document is None:
            raise HTTPException(
                status_code=500,
                detail="Document was not saved."
            )

        return DocumentRead(
            id=document.id,
            name=document.name,
            version=document.version,
        )

    finally:
        db.close()


@router.get("/", response_model=List[DocumentRead])
def list_documents():

    db: Session = SessionLocal()

    try:
        documents = (
            db.query(Document)
            .order_by(Document.version.desc())
            .all()
        )

        return [
            DocumentRead(
                id=d.id,
                name=d.name,
                version=d.version,
            )
            for d in documents
        ]

    finally:
        db.close()