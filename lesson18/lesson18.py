# Lesson 18

num = int(input("Enter an integer greater than 0: "))

for divider in range(1,num+1):
    print(f"Divider variable is {divider}")

    if num % divider == 0:
        print(f"{divider} is a factor for {num}")