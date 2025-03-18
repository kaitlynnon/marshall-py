# Lesson 45

def wordLength(aList):
    return {key : len(key) for key in aList}
print(wordLength(["apple","banana","cherry","date"]))

def dictionaryFib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2,num+1):
            result[i] = result[i-1] + result[i-2]
        return result
print(dictionaryFib(10))