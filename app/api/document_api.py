from pathlib import Path
from typing import List

from fastapi import APIRouter, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document
from app.schemas.document_schema import DocumentCreate, DocumentRead
from app.services.ingest_service import IngestService
from app.services.version_service import VersionService

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/ingest", response_model=DocumentRead)
def ingest_document(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    upload_dir = Path("generated")
    upload_dir.mkdir(exist_ok=True)
    save_path = upload_dir / file.filename

    with save_path.open("wb") as handle:
        handle.write(file.file.read())

    service = IngestService()
    nodes = service.ingest(str(save_path))
    version_service = VersionService()
    document = version_service.create_version(file.filename, 1, nodes)

    db: Session = SessionLocal()
    db.add(document)
    db.commit()
    db.refresh(document)
    db.close()

    return DocumentRead(id=document.id, name=document.name, version=document.version)


@router.get("/", response_model=List[DocumentRead])
def list_documents():
    db: Session = SessionLocal()
    documents = db.query(Document).order_by(Document.version.desc()).all()
    db.close()
    return [DocumentRead(id=item.id, name=item.name, version=item.version) for item in documents]
