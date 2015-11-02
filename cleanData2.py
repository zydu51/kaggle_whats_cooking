# -*- coding: utf-8 -*-

import json

#JSON读取
def json2data(fileName):
    data = json.load(open(fileName,'r',encoding='utf-8'))
    return data

#dict所有原材料
def distAllIngredients(fileName):
    data = json2data(fileName)
    ingreDict = {}
    for item in data:
        ingredients = item['ingredients']
        for ingredient in ingredients:
            if(ingredient not in ingreDict):
            	ingreDict[ingredient] = 1
            else:
            	ingreDict[ingredient] += 1
    return ingreDict

#dict原材料及对应类别
def distIngredientsAndCuisine(fileName):
    data = json2data(fileName)
    ingreAndCuiDict = {}
    for item in data:
        cuisine = item['cuisine']
        ingredients = item['ingredients']
        for ingredient in ingredients:
            if(ingredient not in ingreAndCuiDict):
            	ingreAndCuiDict[ingredient] = {cuisine:1}
            else:
                if cuisine not in ingreAndCuiDict[ingredient]:
                    ingreAndCuiDict[ingredient][cuisine] = 1
                else:
                    ingreAndCuiDict[ingredient][cuisine] += 1
    return ingreAndCuiDict

#list训练数据
def trainJson2List(fileName):
    data = json2data(fileName)
    trainList = []
    for item in data:
        ID = item['id']
        cuisine = item['cuisine']
        ingredients = []
        ingredItems = item['ingredients']
        for ingredient in ingredItems:
            ingredients.append(ingredient)
        trainList.append([ID,cuisine,ingredients])
    return trainList

#list测试数据
def testJson2List(fileName):
    data = json2data(fileName)
    testList = []
    for item in data:
        ID = item['id']
        ingredients = []
        ingredItems = item['ingredients']
        for ingredient in ingredItems:
            ingredients.append(ingredient)
        testList.append([ID,ingredients])
    return testList

#清洗训练list
def trainListClean(trainList,commonIngred):
    cleanedTrainList = []
    for t in trainList:
        ID = t[0]
        cuisine = t[1]
        ingreds = []
        for ingred in t[2]:
            if ingred in commonIngred:
                ingreds.append(ingred)
        cleanedTrainList.append([ID,cuisine,ingreds])
    return cleanedTrainList

#清洗测试list
def testListClean(testList,commonIngred):
    cleanedTestList = []
    for t in testList:
        ID = t[0]
        ingreds = []
        for ingred in t[1]:
            if ingred in commonIngred:
                ingreds.append(ingred)
        cleanedTestList.append([ID,ingreds])
    return cleanedTestList

#读取原材料
trainDict = distAllIngredients('train.json')
testDict = distAllIngredients('test.json')
ingreAndCuiDict = distIngredientsAndCuisine('train.json')

#json转list
trainList = trainJson2List('train.json')
testList = testJson2List('test.json')

#统计训练数据原材料
trainIngred = list(trainDict.keys())
numInTrain = len(trainIngred)
print('训练数据原材料种类：' + str(numInTrain))

#统计测试数据原材料
testIngred = list(testDict.keys())
numInTest = len(testIngred)
print('测试数据原材料种类：' + str(numInTest))

#统计公共原材料
numInTrainAndTest = 0
commonIngred = {}
for key in trainDict:
    if key in testDict:
        numInTrainAndTest += 1
        commonIngred[key] = 1
print('公共原材料种类：' + str(numInTrainAndTest))

#统计特殊原材料
numSpecialIngre = 0
specialIngred = {}
for key in commonIngred:
    if(len(ingreAndCuiDict[key]) == 1):
        numSpecialIngre += 1
        specialIngred[key] = list(ingreAndCuiDict[key].keys())[0]
        #print(str(numSpecialIngre) + ' ' + key + str(ingreAndCuiDict[key]))
print('特殊原材料种类：' + str(numSpecialIngre))

#不剔除特殊原材料
numCleanedCommonIngred = 0
cleanedCommonIngred = {}
for key in commonIngred:
    numCleanedCommonIngred += 1
    cleanedCommonIngred[key] = 1
print('用于训练原材料种类：' + str(numCleanedCommonIngred))


#清洗list
cleanedTrainList = trainListClean(trainList,cleanedCommonIngred)
cleanedTestList = testListClean(testList,cleanedCommonIngred)
cleanedIngred = list(cleanedCommonIngred.keys())

