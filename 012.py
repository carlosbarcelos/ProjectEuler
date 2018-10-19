'''

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
�1: 1�3: 1,3�6: 1,2,3,610: 1,2,5,1015: 1,3,5,1521: 1,3,7,2128: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
'''

import sys

# Returns the sum of the sequence of natural numbers below and including n
def triangle(n):
    sum = 0
    for i in range(n,0,-1):
        sum += i
    return sum

# Returns the number of unique divisors a number has
def numDivisors(n):
      factorList = []
      # Get factors...
      for i in range(1, int(n ** 0.5 + 1)):
          if n % i == 0:
              factorList += [i]
              if (i != n/i):
                  factorList += [n//i]

      return len(factorList)


    for i in range(sys.maxsize):
        t = triangle(i)
        if numDivisors(t) > 500:
            return t
    return -1


