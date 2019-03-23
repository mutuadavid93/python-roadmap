"""
    Collection:
        Rather than a container range is a collection.

    @Syntax:
        range(start, stop, [step])

    Stop Value:
        is one past the end. i.e. (stop - 1).
        This principle is called "half-open".
"""


# When one argument is specified, it starts from 0.
#
# Implicitly assumes start as 0. i.e. range(0, 5)
from_zero = range(5)

# for r in from_zero: print(r, end=" ")


# Passing the range in a list() constructor,
# causes production of each item. Now a list.
resulting_list = list(range(5, 10))

print(resulting_list)


# Start Value of preceding range used as a Start value of Consecutive
# range.
consecutive_range = list(range(10, 15))

print(consecutive_range)


# range also contains a third step argument,
# which specifies the "step" between successive numbers.
stepped_range = list(range(2, 20, 2))

print(stepped_range)



# For Counters: Don't need to use range.
#
# Instead use; enumerate() which yields (index, value) tuples.
#
# NOTE: The result is specifically "Index" not a "Key".
# thus don't be confused to use a Dictionary.
collection = [100, 150, 200]

for p in enumerate(collection): print(p, end=" ", flush=True)


# Or even avoid dealing with the Tuple by using Tuple unpacking.
for index, value in enumerate(collection):
    print("index = {}, value = {}".format(index, value))