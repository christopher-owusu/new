# from pymongo import MongoClient

# client = MongoClient()
# db = client.test  # use a database called "test_database"
# collection = db.test   # and inside that DB, a collection called "files"

# f = open('SpeedRecord.txt')  # open a file
# text = f.read()    # read the entire contents, should be UTF-8 text

# # build a document to be inserted
# text_file_doc = {"file_name": "SpeedRecord.txt"}
# # insert the contents into the "file" collection
# collection.insert(text_file_doc)


from pymongo import MongoClient
client = MongoClient("mongodb+srv://group5:osgroup5project1@project1.radks.mongodb.net/node-tuts?retryWrites=true&w=majority")

db = client.test
files = db.test

f = open('SpeedRecord.txt')
text = f.read()
doc = {
"file_name": "SpeedRecord.txt",
"contents" : text }
files.insert(doc)