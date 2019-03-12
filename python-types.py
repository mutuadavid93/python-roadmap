from decimal import *

# Python Likes Inferring Variable Types by Value Used.

# int, str, bool, NoneType, float

## String Types
x = "sixty eighTy";

firstCharUppercase = x.capitalize();
allUpperCase = x.upper()
lowerCased = x.lower()

# Spaces after a variable "<" or ">" to fill up length
print('Start "{1:<04}" "{0:>9}"'.format(9,888))

print(lowerCased)

## Numeric Types
z = 7 // 3    # truncates the result to an Int
f = 7 / 3     # casts it into a float

# Dealing with Minute Floating Numbers
a = Decimal(".10")
b = Decimal(".30")

sum = a + a + a - b; # prints 0.00

## NoneType: Denotes lack of value.
w = None;

# id() helps differentiate objects
xy = (1, 'two', 3.25, [4,'four'], 99)
yx = (1, 'two', 3.25, [4,'four'], 99)

if xy[2] is yx[2]:
    print("Yeah they are equal.")
else:
    print('Nope they ain\'t equal')

# Checking Type Equivalent:
if isinstance(xy, tuple):
    print("Yeah it's a tuple.")
else:
    print('Aint a tuple type')

print(id(xy[1]))
print(id(yx[1]))