# -*- coding: utf-8 -*-

import json
from pprint import pprint
from xlrd import open_workbook
import numpy as np


X_train =  np.load('xtrain.npy')
X_test =  np.load('xtest.npy')
Y_train = np.load('ytrain.npy')
Y_test = np.load('ytest.npy')

print(len(X_train))
print(len(X_test))
print(len(Y_train))
