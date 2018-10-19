'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
'''
import math
from functools import reduce

MAX_NUM = 500

def findTriplet(a,b,c):
    returnTriplet = None
    lVal = math.pow(a,2) +  math.pow(b,2)
    rVal =  math.pow(c,2)

    if lVal == rVal:
        returnTriplet = [a,b,c]
    return returnTriplet

def compute():
    for a in range(1, MAX_NUM):
        for b in range(a+1, MAX_NUM):
            for c in range(b+1, MAX_NUM):
                triplet = findTriplet(a,b,c)
                if triplet:
                    sumABC = reduce(lambda x, y: x + y, triplet)
                    if sumABC == 1000:
                        return reduce(lambda x, y: x * y, triplet)

if __name__ == '__main__':
	print(compute())

