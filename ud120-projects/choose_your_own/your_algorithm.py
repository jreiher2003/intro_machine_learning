#!/usr/bin/python
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
# 94
#kneighbors
from sklearn import neighbors 
clf = neighbors.KNeighborsClassifier(
	n_neighbors=10, weights='distance', 
	algorithm='auto', leaf_size=30, p=1, 
	metric='minkowski', metric_params=None, 
	n_jobs=1
	)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test) 
from sklearn.metrics import accuracy_score 
print accuracy_score(pred, labels_test, normalize=True)

# 91.8
# GaussianNB
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
# clf.fit(features_train,labels_train)
# pred = clf.predict(features_test)
# from sklearn.metrics import accuracy_score
# print accuracy_score(pred, labels_test, normalize=True)

# 92
# from sklearn import svm
# clf = svm.SVC(
# 	C=1.0, kernel='rbf', degree=3, gamma='auto', 
# 	coef0=0.0, shrinking=True, probability=False, 
# 	tol=0.001, cache_size=200, class_weight=None, 
# 	verbose=False, max_iter=-1, decision_function_shape=None, 
# 	random_state=None)
# clf.fit(features_train,labels_train)
# pred = clf.predict(features_test)
# from sklearn.metrics import accuracy_score
# print accuracy_score(pred, labels_test, normalize=True)

# 92
# from sklearn import tree
# clf = tree.DecisionTreeClassifier(
# 	criterion='gini', splitter='best', max_depth=None, 
# 	min_samples_split=20, min_samples_leaf=2, min_weight_fraction_leaf=0.0, 
# 	max_features=None, random_state=None, max_leaf_nodes=None, 
# 	class_weight=None, presort=True)
# clf.fit(features_train,labels_train)
# pred = clf.predict(features_test)
# from sklearn.metrics import accuracy_score
# print accuracy_score(pred, labels_test, normalize=True)
 
# 92.8
# from sklearn.ensemble import AdaBoostClassifier
# clf = AdaBoostClassifier(
# 	base_estimator=None, n_estimators=20, 
# 	learning_rate=1.0, algorithm='SAMME.R', 
# 	random_state=None)
# clf.fit(features_train,labels_train)
# pred = clf.predict(features_test)
# from sklearn.metrics import accuracy_score
# print accuracy_score(pred, labels_test, normalize=True)

# 93.6
# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(
# 	n_estimators=10, criterion='gini', max_depth=None, 
# 	min_samples_split=20, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
# 	max_features='auto', max_leaf_nodes=None, bootstrap=True, 
# 	oob_score=False, n_jobs=1, random_state=None, 
# 	verbose=0, warm_start=False, class_weight=None
# 	)
# clf.fit(features_train,labels_train)
# pred = clf.predict(features_test)
# from sklearn.metrics import accuracy_score
# print accuracy_score(pred, labels_test, normalize=True)
  
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
