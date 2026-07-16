from typing import List, Dict

from app.models.document import Document


class StalenessService:
    def detect_stale_sections(self, document: Document) -> List[Dict[str, object]]:
        stale_nodes = []
        for node in document.nodes or []:
            if not node.body:
                stale_nodes.append({"heading": node.heading, "reason": "missing body content"})
        return stale_nodes
