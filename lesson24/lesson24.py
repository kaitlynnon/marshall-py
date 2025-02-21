# Lesson 24

name = ''
longestLength = 0
longestName = ''

while name != 'X':
    name = input("Enter your name or 'X' to exit: ")

    if name != 'X':
        currentLength = len(name)

        if currentLength > longestLength:
            longestLength = currentLength
            longestName = name
    else:
        print("End of inputs")

if longestName:
    print(f"The longest name with {longestLength} amount of characters is {longestName}")
else:
    print("Not enough data")

