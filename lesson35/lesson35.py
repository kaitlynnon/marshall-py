# Lesson 35
word = input("Enter a string: ")
def duplicates(aList):
    newList = []
    for item in aList:
        if item not in newList:
            newList.append(item)
    return newList

print(f"The duplicates have been removed: {duplicates(word)}")