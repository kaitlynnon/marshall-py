# Lesson 34
def csvToList(text):
   
    csv = text.split(',')
    aList = []

    for item in csv:
        aList.append(int(item))
    return aList

print(csvToList("1,2,3,4,5"))
