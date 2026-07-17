from datetime import datetime

from pymongo import MongoClient


class MongoDBService:

    def __init__(self):

        self.client = MongoClient("mongodb://localhost:27017")

        self.db = self.client["tri9t_assignment"]

        self.collection = self.db["test_cases"]

    def save_testcases(
        self,
        document_name,
        version,
        section,
        testcases
    ):

        document = {

            "document_name": document_name,

            "version": version,

            "section": section,

            "status": "ACTIVE",

            "generated_at": datetime.utcnow(),

            "test_cases": testcases
        }

        result = self.collection.insert_one(document)

        return result.inserted_id

    def mark_stale(
        self,
        document_name,
        section
    ):

        self.collection.update_many(

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

    def get_testcases(
        self,
        version
    ):

        return list(

            self.collection.find(
                {
                    "version": version
                },
                {
                    "_id": 0
                }
            )

        )