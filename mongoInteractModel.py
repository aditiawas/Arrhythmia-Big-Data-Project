import pymongo
import csv
import json
import numpy

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["BDAProject"]
    coll = db["model"]
    return client,db,coll

def sendToDb(pickle_object):
    client,db,coll=startInteract()
    coll.insert_one({"pickle":pickle_object,"name":"logit"})
def emptyDb():
    client,db,coll=startInteract()
    coll.delete_many({})

def recvAllFromDb():
    client,db,coll=startInteract()
    scheme=[]
    pickle_object = coll.find_one({"name":"logit"})
    return(pickle_object["pickle"])
def printAll():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        scheme.append(i)
    print(scheme) #to check

def findLastId():
    client,db,coll=startInteract()
    getall=coll.find().sort("_id", pymongo.DESCENDING)
    for x in getall:
        return x["_id"]
    else:
        return 0

if __name__=="__main__":
    #emptyDb()
    #sendToDb([{"_id":1,"ques":"Random1"}])
    #sendToDb([{"_id":2,"ques":"Random2"}])
    #print(findLastId())
    emptyDb()
    loadDb()
    recvAllFromDb()
