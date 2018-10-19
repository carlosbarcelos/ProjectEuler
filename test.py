'''
Test Suite

Tests all of the Python modules against their expected answer.
'''

import importlib # Run solutions as modules
import csv       # Read answers CSV file
import math      # Ceiling rounding

def main():
    print('Testing Project Euler Solutions')
    print('P[ass]  |  F[ail]  |  E[Error]  |  .[Nonexistant]  ')
    # Open CSV and read values into dictionary
    with open('answers.csv') as f:
        reader = csv.DictReader(f)
        solutionDict = {int(rows['problem']):int(rows['answer']) for rows in reader}

    # Iterate over dictionary 10 at a time
    maxSolution = max(k for k, v in solutionDict.items())
    resultsPerLine = 10
    cnt = 0
    reportString = f'[1-{resultsPerLine}]\t'
    for i in range(1,int(math.ceil(maxSolution / 10.0))*10 + 1):
        try:
            # Import numbered module and check solution for answer
            problem = str(i)
            padding = '0' * (3-len(problem))
            problemString = padding + problem

            expAnswer = solutionDict[i]
            module = importlib.import_module(problemString)
            actAnswer = module.compute()
            # Report the results
            if actAnswer == expAnswer:
                reportString += 'P '
            else:
                reportString += 'F '
        # Catch well-known exceptions
        except ModuleNotFoundError:
            reportString += '. '
        except KeyError:
            reportString += '. '
        except:
            reportString += 'E '

        # Print out the test report
        if i%10 == 0:
            print(reportString)
            reportString = f'[{i+1}-{i+resultsPerLine}]\t'

if __name__ == '__main__':
    main()
