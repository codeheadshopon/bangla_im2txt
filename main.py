# -*- coding: utf-8 -*-

import json
from pprint import pprint
from xlrd import open_workbook
import numpy as np
from PIL import Image
import cPickle,gzip

def dataset_load(path):
    if path.endswith(".gz"):
        f=gzip.open(path,'rb')
    else:
        f=open(path,'rb')

    if sys.version_info<(3,):
        data=cPickle.load(f)
    else:
        data=cPickle.load(f,encoding="bytes")
    f.close()
    return data


X_train =  np.load('xtrain.npy')
X_test =  np.load('xtest.npy')
Y_train = np.load('ytrain.npy')
Y_test = np.load('ytest.npy')

Train = np.array([np.array(Image.open("images/"+filename)) for filename in X_train])
Test = np.array([np.array(Image.open("images/"+filename)) for filename in X_test])

X_train = Train.astype('float32')
X_test = Test.astype('float32')

total_data = (X_train,Y_train),(X_test,Y_test)
print("Pickling")

f = gzip.open('banglaim2txt'+'.pkl.gz','wb')
cPickle.dump(total_data,f,protocol=2)
f.close()


#After Saving The pickle file please remove above lines, You can read the pickle file by uncommenting the following line Sir 
#(X_train,y_train),(X_test,y_test)=dataset_load('./banglaim2txt.pkl.gz')
