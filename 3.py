'''
Problem 3) Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

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

def compute():
    # Get a list of factors
    factorList = getFactors(600851475143)

    # Reduce the list to prime numbers
    primeFactorList = list(filter(lambda i: isPrime(i), factorList))

    # Return the largest number
    largestPrimeFactor = max(primeFactorList)
    return largestPrimeFactor

if __name__ == '__main__':
    print(compute())
