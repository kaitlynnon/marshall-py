# Lesson 42

def possibleSum(aList,target):
    for i, value in enumerate(aList):
        newTarget = target - value
        if newTarget in aList[i+1:]:
            return True
    return False

test = [1,29,5,3,2499,29492]
target = 6

print(f"Can {target} be made from two unique values in: {test}?")
print(possibleSum(test,target))