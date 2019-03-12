x = 40
y = 50

# if, elif and else

if x < y:
    print(f'{x} < {y} and y is {y}')
elif x > y:
    print('{0} > {1}'.format(x, y))
else:
    print('Do something else.')

# Membership Operator
lst = ["Mattz","Grace","Travis Scott"]
if "Travis Scott" in lst:
    print("In collection")

if "Gray Joy" not in lst:
    print("Not in collection")

qy = "Bob"
qz = "Bob"
qx = "Zob"
present = True

# Identity Operators: is, is not.
# is operator, compares the objects/instances not the values.
if qy is not  qz:
    print("They aint the same instance.")

if qy is qz:
    print("They are the same instance.")

# Logical Operators: or, and, not.
if (qy is qz) and (qy is not qx):
    print("Truthy.")

print(not present)

# Ternery Operator
hungry = True
feed = 'Feed the bear now!' if hungry else 'Do not feed the bear'
print(feed)