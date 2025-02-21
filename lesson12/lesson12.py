# Lesson 12

angle1 = int(input("Enter the degree of the first angle: "))
angle2 = int(input("Enter the degree of the second angle: "))
angle3 = int(input("Enter the degree of the third angle: "))

angleSum = angle1 + angle2 + angle3

if angleSum != 180:
    print("Invalid inputs, enter again")
else:
    if angle1 == angle2 == angle3:
        print("It is equilateral")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print("This is a scalene triangle")
    else:
        print("This is an isosceles triangle")
