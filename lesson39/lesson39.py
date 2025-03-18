# Lesson 39
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

print(f"The greatest common divisor between 100 and 289 is {gcd(100,289)}")