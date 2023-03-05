import pickle
import mongoInteractModel
from sklearn.linear_model import LogisticRegression
import classes
import csv
import numpy

def getResult(url1,url2):
    pickle_object = mongoInteractModel.recvAllFromDb()
    clf = pickle.loads(pickle_object)

    reader=csv.reader(open(url1,"r"),delimiter=",")
    X_test=list(reader)
    X_test=numpy.array(X_test)
    X_test=X_test.astype(numpy.float)

    reader=csv.reader(open(url2,"r"),delimiter=",")
    Y_test=list(reader)
    Y_test=numpy.array(Y_test)
    Y_test=Y_test.astype(numpy.float)

    result = []
    arr = list(clf.predict(X_test))
    for i in range(len(arr)):
        result.append("Classification of record "+str(i+1)+": "+classes.getClass(int(arr[i])))
    score = clf.score(X_test, Y_test)
    result.append("Test Set size = 2")
    result.append("Test Set accuracy = "+str(score*100))
    result.append("Test Set error = "+str((1-score)*100))
    return result

if __name__=="__main__":
    res = getResult("/media/medhini/UbuntuData/D/Sem 7/BDA/HeartProjectBDA/reduced_featuresTEST.csv","/media/medhini/UbuntuData/D/Sem 7/BDA/HeartProjectBDA/target_outputTEST.csv")
    print(res)
