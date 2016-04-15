from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import numpy as np


def test_run():
    iris = datasets.load_iris()
    gnb = GaussianNB()
    y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))

def test_run2():
    x = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])
    y = np.array([1,1,1,2,2,2])
    clf = GaussianNB()
    pred = clf.fit(x,y)
    print clf.predict([[-0.8, -1]])


if __name__ == "__main__":
    # test_run()
    test_run2()