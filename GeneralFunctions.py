import math # Common math functions

# Determine if a number is prime
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
        return True

# Return a list of factors
def getFactors(n):
    factorList = []
    # Get factors...
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            factorList += [i]
            if (i != n/i):
                factorList += [n//i]

                return factorList

# Calculate combinations
def nCr(n, r):
    top = math.factorial(n)
    bottom = math.factorial(r) * math.factorial(n-r)
    return top // bottom
