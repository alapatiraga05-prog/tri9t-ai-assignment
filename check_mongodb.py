from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

print("Databases:")
print(client.list_database_names())

db = client["tri9t_assignment"]

print("\nCollections:")
print(db.list_collection_names())

collection = db["test_cases"]

print("\nDocuments:")
for doc in collection.find():
    print(doc)