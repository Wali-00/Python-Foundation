import numpy as np

data = np.array([
    [9.5,.5,95.5],
    [8.2,1.2,86.4],
    [7.8,1.5,82.1],
    [7.0,1.0,81.0],
    [6.5,2.0,74.5],
    [5.0,1.5,70.0],
    [4.5,3.0,60.5],
    [3.0,2.5,55.0,],
    [2.0,4.0,44.0],
     [1.5,4.5,39.5]
])

#randomizing the dataset
ran_index = np.random.choice(10,size=(10,), replace=False)

data = data[ran_index]

#feature and extraction 
#train, test split
#X_train,y_train,X_test,y_test
X = data[:,:2]
y = data[:,2:]

train_index = int(len(data)*.8)

X_train = X[ :train_index,]
y_train = y[:train_index,]
X_test = X[train_index: ,]
y_test = y[train_index: ,]

#doing this work more easily
from sklearn.model_selection import train_test_split

X = data[: ,:2]
y = data[:, 2:]
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size =0.2)