# Lesson 11

point = input()
point = point.split(' ')
point = list(map(int,point))

x,y = point

if x > 0:
    if y > 0:
        print(f"The point ({x},{y}) is in quadrant 1")
    else:
        print(f"The point ({x},{y}) is in quadrant 4")
else: 
    if y > 0:
        print(f"The point ({x},{y}) is in quadrant 2")
    else:
        print(f"The point ({x},{y}) is in quadrant 3")