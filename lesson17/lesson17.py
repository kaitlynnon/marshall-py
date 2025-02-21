# Lesson 17

num = int(input("Enter thr value of N: "))
totalProduct = 1
multiplier = 1

while multiplier <= num:
    totalProduct = totalProduct*multiplier
    multiplier = multiplier + 1
print(f"The factorial of {num} is {totalProduct}")
