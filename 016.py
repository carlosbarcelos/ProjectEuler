'''
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

def compute():
    v = pow(2,1000)
    sumV = sum(int(i) for i in str(v))
    return sumV

if __name__ == '__main__':
    print(compute())

