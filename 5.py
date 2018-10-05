'''
Problem 5) Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import sys

# Determines if n is evenly divisible by all numbers [min, max]
def isEvenlyDivisible(n, min, max):
    for i in range(min, max+1):
        if not n % i == 0:
            return False
    return True

def getSmallestEvenDivisible(min, max):
    for n in range(1,sys.maxsize):
        if isEvenlyDivisible(n, min, max):
            return n
    return -1 # Error. Ran out of numbers

print(getSmallestEvenDivisible(1, 20))
