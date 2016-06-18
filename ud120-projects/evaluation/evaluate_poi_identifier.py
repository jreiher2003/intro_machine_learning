#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import cPickle as pickle 
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score 

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.3, random_state=42)
#print labels_test

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train) 
pred = clf.predict(features_test) 

print pred,len(pred),sum(pred)
print labels_test, len(labels_test)
 

pred1 = [0.] * len(pred)
print len(pred1)
acc = accuracy_score(pred,labels_test, normalize=True) 
print acc

#precision_score(label_test, pred, average='macro' or 'micro', or weighted)
print precision_score(labels_test, pred, average="binary")
print recall_score(labels_test, pred, average="binary")

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
truelabels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print precision_score(truelabels,predictions, average="binary")
print recall_score(truelabels,predictions, average="binary")