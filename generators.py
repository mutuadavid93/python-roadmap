# NOTE: All generators are iterators

"""
    Explanation:
        Execution occurs till a yield statement is encountered.
        Then on repeat by calling next(generator), it RESUMES
        where it Left off. i.e. the next yeild statement.

    Usage:
        Best when streaming infinite or unknown iterable size.

"""
from sys import stderr

def gen24():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to return")

iterator = gen24()

print(next(iterator))
print(next(iterator))