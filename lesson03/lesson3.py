# Lesson 3
tiles = input("Enter the number of tiles: ")
# input is always a string
tiles = int(tiles)
# sqrt is just exponent of a half
# import math
# calculation = math.sqrt(tiles)
calculation = int((tiles ** 0.5) // 1)

print(f"The maximum side length is: {calculation}")