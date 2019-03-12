# List is Mutable
li = [10,20,30,40]
li[0] = 60

#for i in list:
for i in li:
    print('i is {}'.format(i))

# Tuples are Immutable
tuple = (1,2,3,5,6,7)
for x in tuple:
    print('x is {}'.format(x))

# Range is Immutable
# @Syntax: range(start, size, step)
rnge = range(5, 50, 5)
for z in rnge:
    print('z is {}'.format(z))

# Immutable List:
immutableList = list(range(3))
for w in immutableList:
    print('w is {}'.format(w))

# Dictionary is Mutable
dict = {'one': 1,'two':2, 'three':3}
for key, value in dict.items():
    print('Key: %s and Value: %d'%(key, value))

# Remove a Dictionary Value
dict.pop('two')
print(dict)