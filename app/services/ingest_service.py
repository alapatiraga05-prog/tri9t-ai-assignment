from app.database.database import SessionLocal
from app.models.document import Document
from app.models.node import Node

from app.parser.pdf_parser import PDFParser
from app.services.tree_builder import TreeBuilder
from app.utils.hash_utils import generate_hash


class IngestService:

    def ingest(self, pdf_path: str, document_name: str, version: int):

        db = SessionLocal()

        try:

            # Create document entry
            document = Document(
                name=document_name,
                version=version
            )

            db.add(document)
            db.commit()
            db.refresh(document)

            # Parse PDF
            parser = PDFParser(pdf_path)
            parsed_nodes = parser.parse()

            # Build hierarchy
            builder = TreeBuilder()
            builder.build(parsed_nodes)

            # Store nodes
            node_map = {}

            # First pass: create nodes
            for parsed_node in parsed_nodes:

                db_node = Node(
                    document_id=document.id,
                    heading=parsed_node.heading,
                    level=parsed_node.level,
                    body=parsed_node.body,
                    content_hash=generate_hash(parsed_node.body)
                )

                db.add(db_node)
                db.flush()

                node_map[parsed_node] = db_node

            # Second pass: update parent_id
            for parsed_node in parsed_nodes:

                if parsed_node.parent:

                    db_node = node_map[parsed_node]

                    db_node.parent_id = node_map[parsed_node.parent].id

            db.commit()

            print("Document ingested successfully!")

        finally:
            db.close()