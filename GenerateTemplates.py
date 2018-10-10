'''
Use web scraping to gather the problems from projecteuler.net and create
a solution template from them. This is helpful for having problems offline.
'''

import os                     # File/directory manipulation
import sys                    # Get MAX_INT
import re                     # Regex matching
import requests               # Get a webpage
from bs4 import BeautifulSoup # BeautifulSoup page parsing

# Write the solution template
def writeSolutionTemplate(soup, directory):
    # Get the correct elements from the webpage
    content = soup.find("div", {"id": "content"})

    problemNumber = soup.find("div", {"id": "problem_info"}).find(text=True)
    problemTitle = content.h2.text
    problemInfo = soup.find("div", {"class": "problem_content"}).text

    # Create a new template and write to it
    n = re.search(r'\d+', problemNumber).group()
    fn = f'{n}.py'
    exists = os.path.isfile(fn)
    if exists:
        print(f'{problemNumber}already exists.')
        return 1 # Not a valid problem
    else:
        f = open(directory + '/' + fn, 'w')
        try:
            # Create the problem statment header
            f.write("'''\n\r")
            f.write(f'{problemNumber} {problemInfo}')
            f.write("'''\n\r\n\r")

            # Create the compute() function and main definition
            f.write('def compute():\n\r')
            f.write('\treturn 0\n\r')
            f.write('\n\r')
            f.write("if __name__ == '__main__':\n\r")
            f.write('\tprint(compute())\n\r')
        except UnicodeEncodeError as e:
            print(f'{problemNumber}encountered UnicodeEncodeError')
        f.close()
        return 0 # Success

##########
## Main ##
##########
def main():
    # Create a folder for the templates to reside
    directory = 'Templates'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # For every problem . . .
    for i in range(1,sys.maxsize):
        # . . . request the webpage . . .
        webpage = f'https://projecteuler.net/problem={i}'
        data = requests.get(webpage)
        soup = BeautifulSoup(data.text, 'html.parser')
        msg = soup.find("div", {"id": "message"})

        # . . . abort if we have gone too far.
        if msg:
            print(f'There is no problem {i}')
            return 1 # Not a valid problem

        # . .  . write a new template for the given problem
        writeSolutionTemplate(soup, directory)

    return 0 # Success
##############
## End Main ##
#############

if __name__ == '__main__':
    main()
