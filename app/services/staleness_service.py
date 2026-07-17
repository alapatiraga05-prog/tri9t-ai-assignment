from app.services.mongodb_service import MongoDBService


class StalenessService:

    def __init__(self):
        self.mongo = MongoDBService()

    def mark_stale(self, document_name: str, section: str):

        self.mongo.collection.update_many(
            {
                "document_name": document_name,
                "section": section,
                "status": "ACTIVE"
            },
            {
                "$set": {
                    "status": "STALE"
                }
            }
        )

        print(f"Marked previous test cases as STALE for: {section}")