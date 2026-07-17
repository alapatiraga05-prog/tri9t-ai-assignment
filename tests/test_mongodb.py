from app.services.mongodb_service import MongoDBService


def test_mongodb_connection():

    mongo = MongoDBService()

    assert mongo.collection is not None