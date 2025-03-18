# Lesson 40

def factorsList(num):
    result = []
    for divider in range(1,num+1):
        if num % divider == 0:
            result.append(divider)
    return result

def prime(num):
    return len(factorsList(num)) == 2

def primeList(upperLimit):
    primes = [2]
    if upperLimit == 2:
        return primes
    else:
        for num in range(3,upperLimit,2):
            if prime(num):
                primes.append(num)
        return primes
print(f"All primes under 10: {primeList(10)}")
