from sklearn import svm 
import matplotlib.pyplot as plt

X = [[0, 0], [1,1]]
y = [0, 1] 
clf = svm.SVC(kernel="linear", gamma=1.0) 
clf.fit(X, y) 


print clf 
print clf.predict([2.,2.])