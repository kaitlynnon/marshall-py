# Lesson 28
def isPalindrome(text):
    if not text:
        return True
    elif len(text) < 4:
        return text[0] == text[-1]
    else:
        midpoint = len(text) // 2
        for i in range(0,midpoint):
            left = text[i]
            right = text[-1*i - 1]

            if left != right:
                return False
        return True
print(isPalindrome('racecar'))
