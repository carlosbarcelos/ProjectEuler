'''
Problem 14
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

# Initalize base case
cache = {1:[1]}

# Returns the Colltaz sequence of a number
def collatz(n):
    global cache
    # Check cache
    if n in cache.keys():return n, cache[n]

    chain = [n]
    # Even case
    if n % 2 == 0: recurN, recurChain = collatz(n//2)
    # Odd case
    else: recurN, recurChain = collatz((3*n)+1)
    chain += recurChain
    cache[n] = chain
    return n, chain

def compute():
    global cache
    maxVal = 1000000
    maxN = 0
    maxChain = []
    for i in range(1,maxVal):
        n, chain = collatz(i)
        if len(chain) > len(maxChain):
            maxN = n
            maxChain = chain
    return maxN

if __name__ == '__main__':
	print(compute())
