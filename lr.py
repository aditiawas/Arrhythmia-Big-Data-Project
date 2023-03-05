import numpy
import csv
import math
import operator
import random
import mongoInteractReducedFeatures
import mongoInteractTargetOutput
import pickle
import mongoInteractModel
from sklearn.linear_model import LogisticRegression
mongoInteractReducedFeatures.loadDb()
mongoInteractTargetOutput.loadDb()



#create reduced feature matrix
#reader=csv.reader(open("reduced_features.csv","r"),delimiter=",")
#X=list(reader)
#X=numpy.array(X)
#X=X.astype(numpy.float)

X_train = mongoInteractReducedFeatures.recvAllFromDb()


#create result vector
#reader=csv.reader(open("target_output.csv","r"),delimiter=",")
#Y=list(reader)
#Y=numpy.array(Y)
#Y=Y.astype(numpy.int)
#Y=Y.ravel()

Y_train = mongoInteractTargetOutput.recvAllFromDb()

#X_train=[]
#Y_train=[]
#X_test=[]
#Y_test=[]
#X_train = X[:-4]
#Y_train = Y[:-4]


#c=loadDataset(0.8,X,Y, X_train , Y_train,  X_test,  Y_test)

clf = LogisticRegression(max_iter=100,C=1)
clf.fit(X_train,Y_train)

print()
print("..................................Traing set................................")
print()
clf.fit(X_train, Y_train)
print(clf.predict(X_train))
score = clf.score(X_train, Y_train)
#print("Training Set size = ", c)
print("Training Set accuracy = ", score*100)
print("Training Set error = ", (1-score)*100)

pickle_object = pickle.dumps(clf)
mongoInteractModel.sendToDb(pickle_object)

#print(clf.predict(X_test))
#score = clf.score(X_test, Y_test)
#print("Test Set size = ",X.shape[0]-c)
#print("Test Set accuracy = ", score*100)
#print("Test Set error = ",(1-score)*100)
