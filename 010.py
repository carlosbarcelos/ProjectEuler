'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from GeneralFunctions import isPrime

MAX_NUM = 2000000

def compute():
    sum = 0
    for i in range(MAX_NUM):
        if isPrime(i):
            sum += i
    return sum

if __name__ == '__main__':
	print(compute())

