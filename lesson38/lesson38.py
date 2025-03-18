# Lesson 38

def palindrome(text):
    return text == text[::-1]

palidromeNum = []

for num1 in range(999,99,-1):
    for num2 in range(999,99,-1):
        product = num1*num2

        if palindrome(str(product)):
            palidromeNum.append(product)

print(f"The largest palidromic number is {max(palidromeNum)}")