'''
Timing Tool

Get the execution time for each of the solutions.
Use this to find solutions that need optimization.
'''

import importlib # Run solutions as modules
import csv       # Read answers CSV file
import math      # Ceiling rounding
import time      # Timing function

def main():
    print('Timing Tool')
    print('Solution Number : Time to Complete\n')

    # Open CSV and read values into dictionary
    with open('answers.csv') as f:
        reader = csv.DictReader(f)
        solutionDict = {int(rows['problem']):int(rows['answer']) for rows in reader}

    # Iterate over as many solutions as there exists
    maxSolution = max(k for k, v in solutionDict.items())
    for i in range(1,int(math.ceil(maxSolution / 10.0))*10 + 1):
        try:

            # Import numbered module and time
            problem = str(i)
            padding = '0' * (3-len(problem))
            problemString = padding + problem
            module = importlib.import_module(problemString)

            # Time the execution of the solution
            startTime = time.time()
            actAnswer = module.compute()
            endTime = time.time()

            print(f'Problem {problemString} : %.3f sec' % (endTime - startTime))

        # Catch well-known exceptions
        except ModuleNotFoundError:
            print(f'Module {i} Not Found')
        except KeyError:
            print('Key Error')
        except:
            print('Unexpected Error')

if __name__ == '__main__':
    main()
