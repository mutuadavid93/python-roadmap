"""
    Immutable:
        Once created, the objects within them can't be replaced or removed
        and new elements can't be added.

    Silarity:
        Resemble lists but rather enclosed in Parentheses i.e. "()"

    Single Element Tuple:
        MUST contain a trailing coma e.g ("Makausha",)

    Multiple Elements:
        Delimiting Parentheses on one or more values it's optional in tuples.
        NOTE: The latter happens if there are delimiting coma(s) in returned items.
"""

t = ("Soccer", 0.25, True, 111)

# Accessed by indexes: t[index]
element = t[0]

# Determine number of elements in it. len(t)
total_items = len(t)

# Iterate them using loops
for i in t:
    print(i)

# Extend tuples by concatenating with other tuples.
new_tuple = t + ("Pilsner", 170)

# Repeated using * operator
repeated_tuple = t * 2

# Single Element tuple MUST contain a trailing coma.
single_item_tuple = ("Mwewe",)

# Defining an empty tuple
empty_tuple = ()

# Delimiting Parentheses are optional.
#
# The function minmax returns a Tuple.
def minmax(items):
    return min(items), max(items)

print_minmax = minmax([90,7,92,100])


# Tuple unpacking helps us destructure tuples into indidual variables
lower, highest = minmax([90,7,92,100])


# Create a tuple from a list
from_list = tuple(["Strand", "Alicia", "Nick"])


# Check for Membership using: "in" and "not in" operators
isPresent = 'Present' if 'Alicia' in from_list else 'Absent'


print(isPresent)