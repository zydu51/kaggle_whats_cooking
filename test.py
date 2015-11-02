# -*- coding: utf-8 -*-

from trainSVM import *


#读取测试数据
testNums = len(cleanedTestList)

testX = np.zeros((testNums,dims))
testIDs = []
start = clock()
for (num,test) in zip(range(testNums),cleanedTestList):
    #start = clock()
    testIDs.append(test[0])
    for ingred in test[1]:
        testX[num,ingred2dimDict[ingred]] = 1
    #finish = clock()
    #print(finish-start)
finish = clock()


#用分类器分类
print('训练数据个数： ' + str(len(testX)))
print('开始分类...')
start = clock()
testY = clf.predict(testX)
finish = clock()
print('分类完成!!!')
print('测试用时: ' + str(finish-start))


            

#保存
print('保存结果...')
f = open('result2015-1102-1924.csv','w',encoding='utf-8')
f.write('id,cuisine\n')
for ID,y in zip(testIDs,testY):
    f.write(str(ID) + ',' + y + '\n')
f.close()
print('保存成功!!!')
    

