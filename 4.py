'''
Problem 4) Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Determine if this number is a palindrome
def isPalindrome(n):
    revN = str(n)[::-1]
    return str(n) == revN

largestPalindrome = 0
for i in range(1000):
    for j in range(1000):
        prod = i*j
        if isPalindrome(prod):
            if prod > largestPalindrome:
                largestPalindrome = prod

print(largestPalindrome)
