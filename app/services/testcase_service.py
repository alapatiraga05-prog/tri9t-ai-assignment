from app.services.comparison_service import ComparisonService
from app.services.ai_service import AIService
from app.services.mongodb_service import MongoDBService
from app.services.staleness_service import StalenessService

from app.database.database import SessionLocal
from app.models.node import Node


class TestCaseService:

    def __init__(self):

        self.compare_service = ComparisonService()
        self.ai_service = AIService()
        self.mongo_service = MongoDBService()
        self.staleness_service = StalenessService()

    def generate_for_modified_sections(self, old_version, new_version):

        comparison = self.compare_service.compare(
            version1=old_version,
            version2=new_version
        )

        modified_sections = (
            comparison["modified"] +
            comparison["added"]
        )

        db = SessionLocal()

        try:

            for heading in modified_sections:

                node = (
                    db.query(Node)
                    .filter(
                        Node.document_id == new_version,
                        Node.heading == heading
                    )
                    .first()
                )

                if node is None:
                    continue

                print(f"\nProcessing Section: {heading}")

                # Mark previous ACTIVE test cases as STALE
                self.staleness_service.mark_stale(
                    document_name=f"Document_{new_version}",
                    section=node.heading
                )

                # Generate new AI test cases
                result = self.ai_service.generate_testcases(
                    heading=node.heading,
                    body=node.body
                )

                # Store new ACTIVE test cases
                self.mongo_service.save_testcases(
                    document_name=f"Document_{new_version}",
                    version=new_version,
                    section=node.heading,
                    testcases=result["test_cases"]
                )

                print("New ACTIVE test cases saved.")

            print("\nCompleted generating test cases for all modified sections.")

        finally:
            db.close()