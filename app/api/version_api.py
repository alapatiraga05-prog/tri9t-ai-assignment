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


@router.get("/compare/{version1}/{version2}")
def compare_versions(version1: int, version2: int):

    result = ComparisonService().compare(
        version1=version1,
        version2=version2
    )

    return result