import pymongo
import json
import csv

collNames = ['Age','Sex','Height','Weight','QRS','P-R','Q-T','T','P']

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["BDAProject"]
    coll = db["arrhythmia"]
    return client,db,coll

def loadDb():
    client,db,coll=startInteract()

    with open('arrhythmia.csv', 'r') as csvfile:
    # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data = {}
            counter = 0
            for val in row:
                data[str(counter)] = val
                counter+=1
            js = json.dumps(data)
            coll.insert_one(data)

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
        for j in range(280):
            row.append(i[str(counter)])
            counter += 1
        scheme.append(row)
    print(scheme) #to check

def printAll():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        counter = 0
        row = []
        for j in range(len(i.keys())):
            row.append(i[str(counter)])
            count += 1
        scheme.append(row)
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
    recvAllFromDb()
