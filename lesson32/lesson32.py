# Lesson 32
word1 = input("enter a word: ")
word2 = input("enter another word: ")

def duplicates(word1, word2):

    if not word1 or not word2:
        return []
    else:
        setWord2 = set(word2)
        result = []
        for character in word1:
            if character in setWord2:
                result.append(character)
        return sorted(result)
print(duplicates(word1, word2))