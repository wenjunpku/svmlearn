import pickle as pk
with open('data_X.txt', 'rb') as f:
    train_X = pk.load(f)
with open('data_Y.txt', 'rb') as f:
    train_Y = pk.load(f)
with open('data_X_test.txt', 'rb') as f:
    test_X = pk.load(f)
with open('data_Y_test.txt', 'rb') as f:
    test_Y = pk.load(f)

assert(train_X.shape[0] == train_Y.shape[0] and test_X.shape[0] == test_Y.shape[0])
data = {}

data['train_X'] = train_X

data['train_Y'] = train_Y
data['test_X'] = test_X
data['test_Y'] = test_Y
with open('../data/data.pkl','wb') as f:
    pk.dump(data,f)
