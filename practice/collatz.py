n = int(input("Input a number greater than 0: "))

while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
    elif n % 2 != 0:
        n = 3*n + 1
        print(n)
print("num = 1")