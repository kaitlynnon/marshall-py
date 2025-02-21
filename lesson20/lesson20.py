# Lesson 20

totalSum = 0

for num in range(1,10000):
    factorSum = 0
    for divider in range(1,num):
        if num % divider == 0:
            factorSum += divider

    if factorSum == num:
        totalSum += num
        print(f"{num} is a perfect number")

print(f"The total sum for all perfect numbers under 10000 is {totalSum}")