from typing import List, Optional

from pydantic import BaseModel


class DocumentCreate(BaseModel):
    name: str
    version: int


class DocumentRead(BaseModel):
    id: Optional[int] = None
    name: str
    version: int

    class Config:
        from_attributes = True
