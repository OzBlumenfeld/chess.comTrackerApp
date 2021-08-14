import pymongo
import os

def getDbConnection(db, collection):
    # file = open("dbCredentials.txt", "r")
    # credentials = file.read()
    credentials = os.environ['DB_CREDENTIALS']
    print(credentials)
    client = pymongo.MongoClient(credentials)

    return client[db][collection]
    # db = client["AppDB"]
    # collection =  db["RegisteredUsers"]

def findDocument(collection, json):
    return collection.find_one(json)