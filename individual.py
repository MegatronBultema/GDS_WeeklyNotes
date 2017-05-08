from pymongo import MongoClient
client = MongoClient()
db = client.nyt_dump
coll = db.articles
for document in coll.find():
