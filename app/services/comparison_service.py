from app.database.database import SessionLocal

# Import BOTH models
from app.models.document import Document
from app.models.node import Node


class ComparisonService:

    def compare(self, version1: int, version2: int):

        db = SessionLocal()

        try:

            v1_nodes = (
                db.query(Node)
                .filter(Node.document_id == version1)
                .all()
            )

            v2_nodes = (
                db.query(Node)
                .filter(Node.document_id == version2)
                .all()
            )

            v1 = {
                node.heading: node
                for node in v1_nodes
            }

            v2 = {
                node.heading: node
                for node in v2_nodes
            }

            added = []
            deleted = []
            modified = []
            unchanged = []

            # Compare Version 2 against Version 1
            for heading in v2:

                if heading not in v1:
                    added.append(heading)

                else:

                    if v1[heading].content_hash == v2[heading].content_hash:
                        unchanged.append(heading)
                    else:
                        modified.append(heading)

            # Find deleted sections
            for heading in v1:

                if heading not in v2:
                    deleted.append(heading)

            return {
                "added": added,
                "deleted": deleted,
                "modified": modified,
                "unchanged": unchanged
            }

        finally:
            db.close()