# -*- coding: utf-8 -*-

import json

def json2data(fileName):
    data = json.load(open(fileName,'r',encoding='utf-8'))
    return data

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

def writeDict2File(fileName,Dict):
    f = open(fileName,'w',encoding='utf-8')
    for key in Dict:
        f.write(str(key)+' : '+str(Dict[key])+'\n')
    f.close()

trainDict = distAllIngredients('train.json')
testDict = distAllIngredients('test.json')
ingreAndCuiDict = distIngredientsAndCuisine('train.json')

print('trainDict size is ' + str(len(trainDict)))
print('testDict size is ' + str(len(testDict)))

trainList = trainJson2List('train.json')
testList = testJson2List('test.json')

print('trainList size is ' + str(len(trainList)))
print('testList size is ' + str(len(testList)))



numInTrainNotInTest = 0
for key in trainDict:
    if key not in testDict:
        numInTrainNotInTest += 1
print('numInTrainNotInTest = ' + str(numInTrainNotInTest))

numInTestNotInTrain = 0
for key in testDict:
    if key not in trainDict:
        numInTestNotInTrain += 1
print('numInTestNotInTrain = ' + str(numInTestNotInTrain))

numInTrainAndTest = 0
commonDict = {}
for key in trainDict:
    if key in testDict:
        numInTrainAndTest += 1
        commonDict[key] = 1
print('numInTrainAndTest = ' + str(numInTrainAndTest))

numSpecialIngre = 0
specialDict = {}
for key in commonDict:
    if(len(ingreAndCuiDict[key]) == 1):
        numSpecialIngre += 1
        specialDict[key] = list(ingreAndCuiDict[key].values())[0]
        #print(str(numSpecialIngre) + ' ' + key + str(ingreAndCuiDict[key]))
print('numSpecialIngre = ' + str(numSpecialIngre))

numForSVM = 0
dimDict = {}
for key in commonDict:
    if key not in specialDict:
        dimDict[key] = 1
        numForSVM += 1
print('numForSVM = ' + str(numForSVM))


