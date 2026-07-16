from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document
from app.schemas.document_schema import DocumentRead
from app.services.comparison_service import ComparisonService

router = APIRouter(prefix="/versions", tags=["versions"])


@router.get("/", response_model=List[DocumentRead])
def list_versions():
    db: Session = SessionLocal()
    documents = db.query(Document).order_by(Document.version.asc()).all()
    db.close()
    return [DocumentRead(id=item.id, name=item.name, version=item.version) for item in documents]


@router.get("/compare/{left_id}/{right_id}")
def compare_versions(left_id: int, right_id: int):
    db: Session = SessionLocal()
    left_document = db.query(Document).filter(Document.id == left_id).first()
    right_document = db.query(Document).filter(Document.id == right_id).first()
    db.close()

    if not left_document or not right_document:
        raise HTTPException(status_code=404, detail="One or both documents were not found")

    result = ComparisonService().compare_documents(left_document, right_document)
    return result
