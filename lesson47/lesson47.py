# Lesson 47

def rSum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + rSum(num-1)

print(f"the sum of all numbers from 1-10 is {rSum(10)}")