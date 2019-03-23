# Def: A list created based on another list or an iterator:

# The extra "if clause" is only allowed after the "for clause"

def main():
    seq = range(5)

    # Creating a list Comprehension:
    seq_comprehension = [x * 2 for x in seq]
    seq_divisible_by3 = [x for x in seq if x % 3 == 0]
    with_tuples = [(x, x**2) for x in seq]

    from math import  pi
    pied = [round(pi, i) for i in seq]

    print_comprehension(seq)
    print_comprehension(seq_comprehension)
    print_comprehension(seq_divisible_by3)
    print(with_tuples)
    print(pied)

    # Creating a dictionary Comprehension:
    dict_seq = { x: x**2 for x in seq }

    print(dict_seq)

def print_comprehension(collection):
    for x in collection: print(x, end = ' ')
    print()




##########################
#
#   LIST COMPREHENSION
#
##########################

# @Syntax:
# [ expression for item in list if conditional ]

# @Syntax II
# *result*  = [*transform* *iteration* *filter*]
#
# the "filter" determines if the "transformation" will occur

# Equivalent to:
list = [9,5,6,8]
res = []


for item in list:
    if item % 2 == 0:
        res.append(item)

results = [(item ** 2) for item in list if item % 2 == 0]
new_list = [item for item in list]

print(new_list)

"""
    Nested for loops in List Compression
    
    Trick Shot: Rewrite it in your head as Normal nested for loop Statements
"""
non_flat = [ [1,2,3], [4,5,6], [7,8] ]

flat_list = [y for x in non_flat for y in x]

print(flat_list)



##########################
#
#   SET COMPREHENSION
#
##########################

phrase = "Rewrite it in your head as Normal nested for loop Statement"
words = phrase.split(" ")

words_length = {len(word) for word in words}

print(words_length)



###############################
#
#   DICTIONARY COMPREHENSION
#
###############################
country_to_capital = {"Kenya": "Nairobi","Uganda": "Kampala"}

capital_to_country = {capital:country for country, capital in country_to_capital.items()}

print(capital_to_country)

if __name__ == '__main__': main()