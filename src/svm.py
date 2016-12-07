from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn import metrics
import numpy as np
import codecs
import pickle as pk
import matplotlib.pyplot as plt
with open('../data/data.pkl','rb') as f:
    data = pk.load(f)
train_X = data['train_X']
train_Y = data['train_Y']
test_X = data['test_X']
test_Y = data['test_Y']
clf = svm.LinearSVC(max_iter=3000)
clf.fit(train_X,train_Y)
pre_y = clf.predict(test_X)
print (classification_report(test_Y,pre_y))
