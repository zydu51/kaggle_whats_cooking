# -*- coding: utf-8 -*-

from time import clock

from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_classif
import plot_learning_curve
import numpy as np

from cleanData2 import *

#读取数据为分类器训练数据
nums = len(cleanedTrainList)
dims = len(cleanedIngred)
trainX = np.zeros((nums,dims))
trainY = []
IDs = []

ingred2dimDict = {ingred:dim for ingred,dim in zip(cleanedIngred,range(dims))}
start = clock()
for (num,train) in zip(range(nums),cleanedTrainList):
    #start = clock()
    IDs.append(train[0])
    trainY.append(train[1])
    for ingred in train[2]:
        trainX[num,ingred2dimDict[ingred]] = 1
    #finish = clock()
    #print(finish-start)
finish = clock()

print('训练数据个数： ' + str(len(trainX)))
print('数据维数： ' + str(len(cleanedIngred)))

#开始训练
print('开始训练...')
start = clock()

#tuned_parameters = [{'C': [0.001, 0.01, 0.1, 1, 10]}]
#scores = ['precision', 'recall']

#clf = GridSearchCV(svm.LinearSVC(),tuned_parameters,cv=5,scoring='precision_weighted')
#clf.fit(trainX,trainY)
#for params, mean_score, scores in clf.grid_scores_:
#        print("%0.3f (+/-%0.03f) for %r"
#              % (mean_score, scores.std() * 2, params))

#plot_learning_curve.plot_learning_curve(Pipeline([("fs", SelectKBest(f_classif, k=1000)),("svc", svm.LinearSVC(C=0.1))]),
#                                        "LinearSVC(C=0.1)", trainX, trainY)

clf = svm.LinearSVC(C = 0.1)
clf.fit(trainX,trainY)

finish = clock()
print('训练完成!!!')
print('训练用时: ' + str(finish-start))

    

