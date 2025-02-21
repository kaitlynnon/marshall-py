# Lesson 13

month = int(input("Enter the month (Value from 1-12)"))
date = int(input("Enter the date (Value from 1-31)"))

if month == 2 and date == 18:
    print("Special")
elif month > 2:
    print("After")
elif month == 2 and date > 18:
    print("After")
elif month <= 2:
    print("Before")