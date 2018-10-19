'''
Problem 5) Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import sys

def compute():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i * j) % k == 0:
                    i *= j
                    break
    return i

if __name__ == '__main__':
    print(compute())

''' Original, SLOW solution
# Determines if n is evenly divisible by all numbers [min, max]
def isEvenlyDivisible(n, min, max):
    for i in range(min, max+1):
        if not n % i == 0:
            return False
    return True

def compute():
    rangeMin = 1
    rangeMax = 20
    for n in range(rangeMax,sys.maxsize):
        if isEvenlyDivisible(n, rangeMin, rangeMax):
            return n
    return -1 # Error. Ran out of numbers
'''
