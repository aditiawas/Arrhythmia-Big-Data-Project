import pymongo
import json
import csv
import numpy

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["BDAProject"]
    coll = db["target_output"]
    return client,db,coll

def loadDb():
    client,db,coll=startInteract()

    with open('target_output.csv', 'r') as csvfile:
    # creating a csv reader object
        rowCount = 0
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data = {"_id":rowCount}
            counter = 0
            for val in row:
                data[str(counter)] = val
                counter+=1
            js = json.dumps(data)
            coll.insert_one(data)
            rowCount+=1
def getRecordByClass(c):
    client,db,coll=startInteract()
    classArr = []
    for i in coll.find({"0":str(c)}):
        classArr.append(i["_id"])
    return(classArr)

def emptyDb():
    client,db,coll=startInteract()
    coll.delete_many({})

def recvFromDb(num):
    client,db,coll=startInteract()
    scheme=[]
    scheme.append(coll.find_one({str(num):num}))
    return scheme[0]

def recvAllFromDb():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        counter = 0
        row = []
        for j in range(1):
            row.append(i[str(counter)])
            counter += 1
        scheme.append(row)
    X=numpy.array(scheme)
    X=X.astype(numpy.float)
    #print(X)
    return(X)

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
    #recvAllFromDb()
