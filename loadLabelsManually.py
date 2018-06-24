# -*- coding: utf-8 -*-

import json
from pprint import pprint
from xlrd import open_workbook
import numpy as np

imagelist=[]
testimagelist = []
X = 0
Dict = np.load('worddict.npy').item()
labels = []
testlabels = []
def fromJsonTrain():
    with open('combined.json') as f:
        data = json.load(f)
    global X
    for i in range(15700):

        labels.append([])
        K = str(i) + ".png"
        imagelist.append(K)
        words = data[K].split()
        for j in words:
            labels[X].append(Dict[j])
        X=X+1
def fromJsonTest():
    with open('combined.json') as f:
        data = json.load(f)
    global X
    Z = 0
    for i in range(15700,15998):

        testlabels.append([])
        K = str(i) + ".png"
        testimagelist.append(K)
        words = data[K].split()
        for j in words:
            testlabels[Z].append(Dict[j])
        Z=Z+1
def fromXcel1():
    i = 0
    wb = open_workbook('an1.xlsx')
    for s in wb.sheets():
        # print 'Sheet:',s.name
        values = []
        # print(s.nrows)
        remaining_images=[]
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value = (s.cell(row, col).value)
                # print(value)

                try:
                    value = str(int(value))
                except:
                    pass
                col_value.append(value)
                # print(col_value)
            values.append(col_value)
        lab = []
        global X
        for val in values:
            if(len(val[1])!=0):
                labels.append([])
                imagelist.append(val[0])
                words = val[1].split()
                for j in words:
                    labels[X].append(Dict[j])
                X+=1
        break

def fromXcel2():
    i = 0
    wb = open_workbook('an2.xlsx')
    for s in wb.sheets():
        # print 'Sheet:',s.name
        values = []
        # print(s.nrows)
        remaining_images = []
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value = (s.cell(row, col).value)
                # print(value)

                try:
                    value = str(int(value))
                except:
                    pass
                col_value.append(value)
                # print(col_value)
            values.append(col_value)
        lab = []
        global X
        for val in values:
            if (len(val[1]) != 0):
                labels.append([])
                imagelist.append(val[0])
                words = val[1].split()
                for j in words:
                    labels[X].append(Dict[j])
                X += 1
        break
fromJsonTrain()
fromXcel1()
fromXcel2()
fromJsonTest()

X_train = imagelist
X_test = testimagelist
Y_train = labels
Y_test = testlabels

np.save('xtrain.npy', X_train)
np.save('xtest.npy', X_test)
np.save('ytrain.npy', Y_train)
np.save('ytest.npy', Y_test)
