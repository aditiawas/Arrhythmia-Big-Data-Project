import csv
import numpy
reader=csv.reader(open("reduced_features.csv","r"),delimiter=",")
X=list(reader)
X=numpy.array(X)
X=X.astype(numpy.float)
print(X)
