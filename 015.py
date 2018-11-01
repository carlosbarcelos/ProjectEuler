'''
Problem 15
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
'''
import GeneralFunctions

# There are NxM steps to get to the end. There are two decisions at every step
# This is a nCr problem where n = NxN and r = N
def compute(N, s):
    return GeneralFunctions.nCr(N*2, s)

if __name__ == '__main__':
	print(compute(20,20))

