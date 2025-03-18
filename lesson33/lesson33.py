# Lesson 33
def mean(aList):
    return sum(aList) / len(aList)
def median(aList):
    sorted_aList = sorted(aList)
    middle = len(aList) // 2

    if len(aList) % 2 == 0:
        [1,2,3,4,5,6]
        left = sorted_aList[middle-1]
        right = sorted_aList[middle]
        return (left+right) / 2
    else:
        return sorted_aList[middle]

from random import seed
from random import randrange

seed(1)
data = [randrange(1,100) for _ in range(randrange(10,30))]
print(f"The random dataset is {data}")
print(f"The sorted dataset is {sorted(data)}")
print(f"The mean of the dataset is {mean(data)}")
print(f"The median of the dataset is {median(data)}")