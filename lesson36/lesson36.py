# Lesson 36
numbers = int(input("Enter a number you'd like to check: "))

def factors(num):
    result = []
    for divider in range(1,num+1):
        if num % divider == 0:
            result.append(divider)
    return result
def prime(num):
    return len(factors(num)) == 2

print(f"The factors are: {factors(numbers)}")
print(f"Is it prime? {prime(numbers)}")