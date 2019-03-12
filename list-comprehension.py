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

if __name__ == '__main__': main()