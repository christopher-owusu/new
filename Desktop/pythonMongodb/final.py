import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://group5:osgroup5project1@project1.radks.mongodb.net/node-tuts?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

file = open('SpeedRecord.txt', 'r')

read = file.read()

# print(read)

# text_file_doc = {"file_name": "SpeedRecord.txt"}

collection.insert(read)

