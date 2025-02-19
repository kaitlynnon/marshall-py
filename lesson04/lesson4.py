# Lesson 4
import math

section1 = input("Enter the number of planks as F: ")
section2 = input("Enter more planks as F: ")
section3 = input("Enter more planks as F : ")

cans = len(section1) + len(section2) + len(section3)
boxes = math.ceil(cans / 12)
leftover = 12*boxes - cans

totalCost = 14.95*boxes

print(f"You need {cans} paint cans")
print(f"You have {leftover} leftover")
print(f"The project costs ${totalCost}")
