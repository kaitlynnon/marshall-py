# Lesson 23

loop = True

totalSum = 0
counter = 0

while loop:
    userInput = input("Enter the numbers and say Exit when you want to stop: ")
    if userInput.lower().capitalize() == "Exit":
        loop = False
    else:
        mark = int(userInput)
        if 0 <= mark <= 100:
            totalSum += mark
            counter += 1
        else:
            print("invalid input")

average = totalSum/counter
print(f"The average is {average}")
