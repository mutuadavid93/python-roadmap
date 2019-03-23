# Handling Exceptions:

"""
    Always use the Standard Exceptions Built into Python,
    unless you have to create your own (i.e. Rare case)
"""

"""
    NOTE: It's never worth checking against Types. ain't
    worth it. Do not raise TypeError Exceptions.
"""

from sys import stderr

def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'.format(str(e)), file=stderr)
    finally:
        print('Always executes no matter what happens '
              'inside try except block')

def main():
    convert({"animal": "cow"})

if __name__ == '__main__': main()