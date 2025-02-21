# Lesson 19

num = int(input("Enter the value of N: "))
counter = 0

for divider in range(1,num+1):
    if num % divider == 0:
        counter += 1

if counter == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a composite number")
