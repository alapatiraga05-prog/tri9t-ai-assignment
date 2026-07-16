from typing import List

from app.models.document import Document
from app.models.node import Node


class VersionService:
    def create_version(self, name: str, version: int, nodes: List[Node]):
        document = Document(name=name, version=version)
        document.nodes = nodes
        return document

    def get_latest_version(self, documents: List[Document]):
        if not documents:
            return None
        return max(documents, key=lambda doc: doc.version)
