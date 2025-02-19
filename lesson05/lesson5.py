# Lesson 5
import math

money = float(input("Enter the amount of money you started with: "))
allCookies = input("Enter the total amount of cookies: ")

bigCookie = allCookies.count("b")
smallCookie = allCookies.count("c")

totalCookies = bigCookie + smallCookie

profit = (bigCookie*2 + smallCookie*1.25) - (bigCookie*0.75 + smallCookie*0.5)

amountAfter = money + profit

print (f"The total amount of cookies is {totalCookies}")
print(f"The profit of of the cookies is {profit}")
print(f"The profit after the cookie sale is ${amountAfter}")