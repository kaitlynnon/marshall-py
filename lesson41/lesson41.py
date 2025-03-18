# Lesson 41

def scrabble(word):
    totalScore = 0
    for character in word: 
        currentChar = character.upper()
        if currentChar in "EAIONRTLSU":
            totalScore += 1
        elif currentChar in "DG":
            totalScore += 2
        elif currentChar in "BCMP":
            totalScore += 3
        elif currentChar in "FHVWY":
            totalScore += 4
        elif currentChar == "K":
            totalScore += 5
        elif currentChar in "JX":
            totalScore += 8
        elif currentChar in "QZ":
            totalScore += 10
    return totalScore

def bestScore(aList):
    resultList = ["", 0]
    for word in aList:
        currentScore = scrabble(word)

        if currentScore > resultList[1]:
            resultList[0] = word
            resultList[1] = currentScore
    return resultList

words = ['despair','choose','notice','history','appetite','dominant','bunny','implicit','prediction',]

answer, score = bestScore(words)
print(f"{answer} has the highest scrabble score: {score}")