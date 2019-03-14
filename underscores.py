"""
    Underscores:

    Single Underscore: A convention that the
    value contained is temporary or insignificant.

    Keyword Collision: Trailing underscore; "class_"
    Mostly if you happen to use reserved Keywords in your program names.

    Mangling: Python Interpreter adds a _ClassName chunk infront of attributes
    marked with leading double underscore to avoid Conflicts.
    i.e. _Foo.__mangled from __mangled.

    Magic Methods: Start and End with leading Double underscores.
    Caution: Never get used to using such in your program to avoid collision with
    the language in the future upgrades.
"""

# "Tuple Unpacking" values into individual variables:
name, age, _ = ('Pavlin', 25, 'brown')

# Trailing Underscore
foo = lambda class_: class_


# Leading Double Underscore
class Foo:
    def __init__(self):
        self.__mangled = 42

    def bar(self):
        return self.__mangled


fooed = Foo()
print(fooed.bar())