from sklearn import linear_model
clf = linear_model.Lasso(alpha=0.1)
clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])



print(clf.coef_)

print(clf.intercept_)

print "predicting"
print clf.predict([[2,4]])