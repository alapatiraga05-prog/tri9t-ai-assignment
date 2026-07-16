from typing import List, Dict

from app.models.document import Document


class AIService:
    def generate_testcases(self, document: Document) -> List[Dict[str, str]]:
        nodes = document.nodes or []
        cases = []
        for idx, node in enumerate(nodes[:10], start=1):
            cases.append(
                {
                    "title": f"Test case {idx}: {node.heading}",
                    "description": node.body or f"Validate section '{node.heading}'",
                }
            )
        return cases
