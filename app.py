from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database"]
collection = db["your_collection"]

print(collection.count_documents({}))  # should be > 0
for doc in collection.find().limit(5):
    print(doc)
