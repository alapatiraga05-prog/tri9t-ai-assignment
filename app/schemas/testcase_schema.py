from typing import List, Optional

from pydantic import BaseModel


class TestCaseRead(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    document_id: Optional[int] = None

    class Config:
        from_attributes = True
