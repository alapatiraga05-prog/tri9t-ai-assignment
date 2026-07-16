from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document
from app.services.ai_service import AIService

router = APIRouter(prefix="/testcases", tags=["testcases"])


@router.post("/generate")
def generate_testcases(document_id: int):
    db: Session = SessionLocal()
    document = db.query(Document).filter(Document.id == document_id).first()
    db.close()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return AIService().generate_testcases(document)
