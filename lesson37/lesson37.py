# Lesson 37

def strZip(text):
    result = ''
    counter = 1

    for i in range(1,len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            result += text[i-1]
            result += str(counter)
            counter = 1
    result += text[-1] + str(counter)

    if len(result) < len(text):
        return result
    else:
        return text

testy = ["kkkaaaiiiitlynnnn"]

for i, testy in enumerate(testy):
    output = strZip(testy)
    print("Test 1: ")
    print(f"Inputted value: {testy}")
    print(f"Outputted value: {output}")