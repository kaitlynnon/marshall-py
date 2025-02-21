# Lesson 10

digit = input("Enter the last 4 digits of the number: ")

if digit[0] in {'8','9'}:
    if digit[-1] in {'8','9'}:
        if digit[1] == digit[2]:
            print("This is a telemarketers number")
        else:
            print("This is not a telemarketers number")
    else:
        print("This is not a telemarketers number")
else:
    print("This is not a telemarketers number")
