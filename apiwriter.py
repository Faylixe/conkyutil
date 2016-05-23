#!/usr/bin/python

""" Simple script that generate API from Conky variable documentation page. """

import requests
from bs4 import BeautifulSoup

def getAPI():
    response = requests.get('http://conky.sourceforge.net/variables.html')
    document = BeautifulSoup(response.text, 'html.parser')
    headerSeen = False
    variables = []
    for row in document.find_all('tr'):
        if not headerSeen:
            headerSeen = True
        else:
            cells = row.findAll('td')
            if len(cells) == 3:
                variables.append(cells)
    return variables

#
FUNCTION_TEMPLATE = """\tdef %s(self):
\t\t\"\"\" %s \"\"\"
\t\tself.writeCommand('%s')
\t\treturn self

"""

if __name__ == '__main__':
    variables = getAPI()
    with open('conkyutil.py', 'w') as file:
        for variable in variables:
            command = variable[0].text
            description = " ".join(variable[2].text.replace('\n', '').split())
            function =  FUNCTION_TEMPLATE % (command, description, command)
            file.write(function)
