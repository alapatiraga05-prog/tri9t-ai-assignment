from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(Integer, ForeignKey("documents.id"))

    heading = Column(String, nullable=False)

    level = Column(Integer, nullable=False)

    body = Column(Text)

    content_hash = Column(String)

    parent_id = Column(Integer, ForeignKey("nodes.id"), nullable=True)

    document = relationship("Document", back_populates="nodes")

    parent = relationship(
        "Node",
        remote_side=[id],
        backref="children"
    )