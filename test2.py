import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test_db
collection = db['test_coll']
doc = {"name":"Иван", "surname":"Иванов"}
collection.save(doc)