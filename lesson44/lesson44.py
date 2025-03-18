# Lesson 44
def cFrequency(word):
    cleanWord = sorted(word.lower())

    answer = {}

    for character in cleanWord:
        if character not in answer:
            answer[character] = 1
        else:
            answer[character] += 1
    return answer

result = cFrequency("kaitlynnn")
print(f"Character frequency of kaitlynnn: {result}")