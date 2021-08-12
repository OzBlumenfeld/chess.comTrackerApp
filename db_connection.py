import pymongo

def getDbConnection(db, collection):
    file = open("dbCredentials.txt", "r")
    credentials = file.read()
    client = pymongo.MongoClient(credentials)

    return client[db][collection]
    # db = client["AppDB"]
    # collection =  db["RegisteredUsers"]

def findDocument(collection, json):
    return collection.find_one(json)