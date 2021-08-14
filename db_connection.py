import pymongo
import os


def getDbConnection(db, collection):
    credentials = os.environ['DB_CREDENTIALS']
    print(credentials)
    client = pymongo.MongoClient(credentials)
    return client[db][collection]


def findDocument(collection, json):
    return collection.find_one(json)
