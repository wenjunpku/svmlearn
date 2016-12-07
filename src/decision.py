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
num = np.sum(train_Y == 1)
assert(train_X.shape[0] == train_Y.shape[0] and test_X.shape[0] == test_Y.shape[0])
x = []
y = []
maxx = 0;
pos = 0;
def classfier(minsplit):
    clf = DecisionTreeClassifier(min_samples_split=minsplit,min_samples_leaf=5, max_depth= 3)
    clf = clf.fit(train_X, train_Y)
    with open("iris.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)
    pri_y = clf.predict(test_X)

    print minsplit,
    res = metrics.accuracy_score(test_Y, pri_y)
    if res > max:
        maxx = res
        pos = minsplit
    x.append(minsplit)
    y.append(res)
    print res;

    #print (classification_report( test_Y,pri_y))
    return res;
for i in range(2,500):
    classfier(i)
'''
#figure the relationship between precision and max_depth ,min_samples_split,min_samples_leaf
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x,y,'g--')
ax.set_title('Precision with the Change of min_samples_split')
plt.xlabel('min_samples_split')
plt.ylabel('Precision')
#plt.show()
plt.savefig('Precison-min_samples_split.pdf')
print 'end'
'''
#print (classification_report( test_Y,pri_y)]
