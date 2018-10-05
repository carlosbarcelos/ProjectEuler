'''
Problem 1) Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
MAX_NUM = 1000
sumMultiples = 0

for i in range(MAX_NUM):
    if (i%3==0) or (i%5==0):
        sumMultiples += i

print(f'Sum of multiples of 3 or 5 below {MAX_NUM} = {sumMultiples}')
