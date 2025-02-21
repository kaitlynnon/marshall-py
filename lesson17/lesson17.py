# Lesson 17

num = int(input("Enter thr value of N: "))
totalProduct = 1
multiplier = 1

while multiplier <= num:
    totalProduct = totalProduct*multiplier
    multiplier = multiplier + 1
print(f"The factorial of {num} is {totalProduct}")

answer2 = 1

for i in range(num,0,-1):
    answer2 *= i
print(f"The factorial of {num} is {answer2}")

answer3 = 1
for j in range(1,num+1):
    answer3 *= j
print(f"The factorial of {num} is {answer3}")
