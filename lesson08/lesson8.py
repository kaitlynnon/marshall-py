# Lesson 8
winCounter = 0

for i in range(6):
    currentResult = input(f"Enter the game {i + 1} result: ")

    if currentResult == "w":
        winCounter += 1

group = 0
if winCounter > 4:
    group = 1
elif winCounter > 2:
    group = 2
elif winCounter > 0:
    group = 3

if group == 0:
    print("The player is eliminated")
else:
    print(f"The player is placed in {group}")