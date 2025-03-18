# Lesson 43

def removeDuplicates(aList):
    return list(set(aList))
print(removeDuplicates([1,1,1,2,2,2,234,34,4,4,4,5,6,7,8,7]))

def uniqueLetters(bList):
    resultSet = set()
    for word in bList:
        tmpSet = set(word)
        resultSet = resultSet | (tmpSet)
    return resultSet
test1 = ["hello","boo","kaitlyn","marshmallow"]
print(uniqueLetters(test1))

def iCount(cList):
    if cList:
        resultSet = cList[0]
        for exampleSet in cList[1:]:
            resultSet = resultSet & exampleSet

test2 = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(iCount(test2))