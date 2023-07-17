import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://group5:osgroup5project1@project1.radks.mongodb.net/node-tuts?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {"_id": 1, "name": "maa", "value": 1} 

collection.insert_one(post)

