'''
Problem 7) 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import sys

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

def compute():
    numberPrime = 0
    for n in range(1,sys.maxsize):
        if isPrime(n):
            numberPrime += 1
            if numberPrime == 10001:
                return n
    return -1 # Error. Ran out of numbers

if __name__ == '__main__':
    print(compute())
