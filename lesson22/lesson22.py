# Lesson 22

upperLimit = int(input("Enter N: "))
fib0 = 0
fib1 = 1
fibn = 0

for n in range(2,upperLimit+1):
    fibn = fib1 + fib0
    fib0 = fib1
    fib1 = fibn

print(f"Fibbonaci number {upperLimit} is {fibn}")