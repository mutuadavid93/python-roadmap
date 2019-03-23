"""
    Immutability:
        The Set Data Structure is Mutable but it's Elements are Immutable.

    Similar:
        Close to Dictionary assemblance but the Elements are Individuals
        without Keys.

    Empty Set:
        Empty "{}" creates a Dictionary hence use the set() constructor.

    Unordered:
        Sets don't follow any order during output.
"""

# Can convert any data structure into a set:
players_list = ["Lonzo", "Klay", "Steph", "Jrue", "Embiid", "Klay"]

clean_list = set(players_list)

# Adding multiple elements from another Set
new_set = set(["Tatum"])
new_set.update(["Green", "Smith"])

# Check Membership/Containment
isPresent = 'Present' if "Jrue" in clean_list else 'Absent'

print(new_set)

# Sets are like Lists which DO NOT ALLOW DUPLICATE Elements

# NOTES: Separated By Commas Enclosed in Curly Braces.
my_set = {20, 2.5, True, "Bone","Bone"}

# Create empty Set
set_definition = set()

##################################
#
#       Basic Operations:
#
##################################

# Add Values one By one
set_definition.add("Rug")
set_definition.add("Mat")

# Add one set values into another set
set_definition.update(my_set)

# Copy one set into another without changing the original set
set_copy = my_set.copy()
set_copy.add("Goat")

# The set() constructor can also be used to copy
new_copy = set(my_set)

print(f'Original Set: {my_set} and Copied Set: {set_copy}')

# Get a Set's length
len(set_definition)

# Remove an Element from a Set
set_definition.remove("Bone")

# Discard also removes an element from a set
set_definition.discard(True)

# NOTE: If the Element is Missing remove() raises an Exception
# whilst discard doesn't throw an Exception.

# Clear: Removes all elements from the Set
set_definition.clear()


scores = [94,67,27,78]

# Get Maximum Value
maxim_value = max(scores)

# Minimum Value
minim_value = min(scores)

# Summation of set values
total = sum(scores)

##################################
#
#       Advanced Operations:
#
##################################

# issubset(), Every element in setA must be present in setB
setA = {1,2,3,7}
setB = {1,2,4,5,3}

is_subset = setA.issubset(setB)
is_still_subset = (setA <= setB)

# issuperset(), Every element in setA must be Present in setB
is_superset = setB.issuperset(setA)
is_still_superset = (setB >= setA)

# UNION: A new set will be created with all elements of setA and setB
# without duplication.
union_set = setA.union(setB)
also_union_set = (setA | setB)

# INTERSECTION: Elements that are available in BOTH setA and setB
# i.e. Common Elements
intersections = setA.intersection(setB)
also_intersections = (setA & setB)

# DIFFERENCE: Common elements will be removed and remaining elements
# will be printed.

# Example: All elements of setA except the common ones will be printed
# in our our case it's empty set.
diff_1 = setA.difference(setB)
also_diff_1 = (setA - setB)

# Example: All elements of setB except the common ones will be printed
diff_2 = setB.difference(setA)
also_diff_2 = (setB - setA)

# SYMMETRIC DIFFERENCE: All elements of BOTH the sets except the common ones.

# Example: All elements of both setA and setB except the common elements
sym_diff = setA.symmetric_difference(setB) # {4, 5, 7}
also_sym_diff = (setA ^ setB)


print(sorted(also_sym_diff))