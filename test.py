'''
Test Suite

Tests all of the Python modules against their expected answer.
'''

import importlib # Run solutions as modules
import csv       # Read answers CSV file

def main():
    print('Testing Project Euler Solutions')
    print('P[ass]  |  F[ail]  |  T[imeout]  |  N[onexistant]')
    # Open CSV and read values
    with open('answers.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Import numbered module and check solution for answer
                problem = row['problem']
                expAnswer = row['answer']
                module = importlib.import_module(f'{problem}')
                actAnswer = str(module.compute())
                # Report the results
                if actAnswer == expAnswer:
                    print(f'{problem}: P')
                else:
                    print(f'{problem}: F')
            # Catch well-known exceptions
            except ModuleNotFoundError:
                print(f"Module {row['problem']} not found")
            except AttributeError:
                print(f'Module {problem} has no attribue compute()')
            # TODO: Create timeout exception


if __name__ == '__main__':
    main()
