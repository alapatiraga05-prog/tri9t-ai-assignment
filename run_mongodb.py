from app.services.mongodb_service import MongoDBService

db = MongoDBService()

sample = [
    {
        "title": "Verify E1 Error",
        "type": "Functional",
        "priority": "High",
        "expected_result": "Device displays E1"
    }
]

id = db.save_testcases(
    document_name="CT200 Manual",
    version=2,
    section="4.2 Error Codes",
    testcases=sample
)

print("Inserted ID:", id)