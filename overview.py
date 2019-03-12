# This is a Comment:

import platform

def messageFunction():
    version = platform.python_version()
    print('Python version {}'.format(version))

def greeting():
    time = 'Morning'
    print(f'Good {time}')   # "Good Morning"

messageFunction()
greeting()