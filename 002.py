'''
Problem 2) Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

def fib(MAX_NUM):
    fibList = []

    fib1 = 1
    fibList += [fib1]
    fib2 = 2
    fibList += [fib2]

    while fib2 < MAX_NUM:
        temp = fib1
        fib1 = fib2
        fib2 += temp
        fibList += [fib2]

    return fibList

def compute():
    MAX_NUM = 4000000
    # Get the sequence up to the max number
    fibList = fib(MAX_NUM)

    # Sum all even values
    sumEven = 0
    for i in fibList:
        if i % 2 == 0:
            sumEven += i
    return sumEven

if __name__ == '__main__':
    print(compute())