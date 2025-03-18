# Lesson 26
def isDivisible(num1,num2):
    return num1 % num2 == 0

def factorCount(number):
    counter = 0
    for divider in range(1, number+1):
        if isDivisible(number, divider):
            counter += 1
    return counter

upperLimit = int(input("Enter N: "))
for num in range(1, upperLimit+1):
    factorSize = factorCount(num)

    print(f"{num} has {factorSize} factors.")