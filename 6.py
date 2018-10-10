'''
Problem 6) Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

def squareOfSums(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return pow(sum,2)

def sumOfSquares(n):
    sum = 0
    for i in range(n+1):
        sum += pow(i,2)
    return sum

def compute():
    n = 100
    return squareOfSums(n) - sumOfSquares(n)

if __name__ == '__main__':
    print(compute())
