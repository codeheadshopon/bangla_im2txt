# -*- coding: utf-8 -*-

import json
from pprint import pprint
from xlrd import open_workbook
import numpy as np
from PIL import Image

X_train =  np.load('xtrain.npy')
X_test =  np.load('xtest.npy')
Y_train = np.load('ytrain.npy')
Y_test = np.load('ytest.npy')

Train = np.array([np.array(Image.open("dataset/"+filename)) for filename in X_train])
Test = np.array([np.array(Image.open("dataset/"+filename)) for filename in X_test])