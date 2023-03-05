import pymongo
import csv
import json
import numpy
import mongoInteractTargetOutput

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["BDAProject"]
    coll = db["reduced_features"]
    return client,db,coll

def loadDb():
    client,db,coll=startInteract()
    with open('reduced_features.csv', 'r') as csvfile:
        rowCount = 0
    # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data = {"_id":rowCount}
            counter = 0
            for val in row:
                data[str(counter)] = float(val)
                counter+=1
            coll.insert_one(data)
            rowCount+=1
def getMinFeature(c,feature):
    client,db,coll=startInteract()
    classArr = mongoInteractTargetOutput.getRecordByClass(c)
    for i in coll.aggregate([{"$match" : {"_id":{"$in":classArr}}},{"$group":{"_id": {},"minPrice": { "$min": "$"+feature }}}]):
        return(i['minPrice'])

def getMaxFeature(c,feature):
    client,db,coll=startInteract()
    classArr = mongoInteractTargetOutput.getRecordByClass(c)
    #print(classArr)
    for i in coll.aggregate([{"$match" : {"_id":{"$in":classArr}}},{"$group":{"_id": {},"maxPrice": { "$max": "$"+feature }}}]):
        return(i["maxPrice"])
def getAvgFeature(c,feature):
    client,db,coll=startInteract()
    classArr = mongoInteractTargetOutput.getRecordByClass(c)
    for i in coll.aggregate([{"$match" : {"_id":{"$in":classArr}}},{"$group":{"_id": {},"avgPrice": { "$avg": "$"+feature }}}]):
        return(i['avgPrice'])

def emptyDb():
    client,db,coll=startInteract()
    coll.delete_many({})

def recvFromDb(num):
    client,db,coll=startInteract()
    scheme=[]
    scheme.append(coll.find_one({"_id":num},{"_id": 0,"question":0,"marks":0}))
    return scheme[0]

def recvAllFromDb():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        counter = 0
        row = []
        for j in range(175):
            row.append(i[str(counter)])
            counter += 1
        scheme.append(row)
    X=numpy.array(scheme)
    X=X.astype(numpy.float)
    print(X)
    return(X)
def printAll():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        scheme.append(i)
    print(scheme) #to check
if __name__=="__main__":
    #emptyDb()
    #sendToDb([{"_id":1,"ques":"Random1"}])
    #sendToDb([{"_id":2,"ques":"Random2"}])
    #print(findLastId())
    emptyDb()
    loadDb()
    #getAvgFeature(1,"0")
