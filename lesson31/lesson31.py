# Lesson 31
input1 = input("Enter a string: ")
input2 = input("enter another string: ")
i = 0
word1 = sorted(input1)
word2 = sorted(input2)
if word1 == word2:
    print("its an anagram ")
elif len(word1) != len(word2):
    print("These are not anagrams")
else:
    print("These are not anagrams")