from decorators import padding


"""
    Unique Keys.
        Otherwise the last item with the same key overwrites those existing.
        
    Immutable Keys:
        Strings, Numbers and Tuples are fine. Mutables e.g. lists are Avoided.
        
    Unordered:
        Never rely on the items order they vary from time to time.
        
    Update by Merging:
        The update replaces values corresponding to the duplicate keys.
"""



@padding
def createDictionary():
    creatures = {"Human": "Mammal", "Alligator": "Reptile", "HornBill": "Bird"}

    # Keys Must always be Immutables: e.g. Strings and Integers
    humans = {45 : "Ball", "KSH": 45000}

    print(humans[45])  # 'Ball'

    # The dict() constructor accepts:
    #
    # 1. iterable series of key-value 2-tuples:
    names_and_ages = [("Lonzo", 37), ("Kuzma", 19), ("Beasely", 26), ("Ingram", 30)]
    players_ages = dict(names_and_ages)

    # 2. keyword arguments
    crops = dict(citrus="Orange", vegetable="Amaranthus")

    # display_dict(creatures)
    # keyCommaValue(crops)

def display_dict(animals):
    for animal in animals: print('%s : %s' %(animal,animals[animal]))

def keyCommaValue(collection):
    # Print Key and Value
    for key, value in collection.items():
        print(f'Key : {key} and Value: {value}')

    # Print Only The Keys.
    #
    # NOTE: iterating by keys isn't always used since default dict
    # iteration is by keys.
    for key in collection.keys(): print(key)

    # Print only The Values
    for value in collection.values(): print(value)


"""
    Dictionary Operations:
"""
# Get value at Specific index
families = {"reptile": "Snake", "mammal": "Whale"}
atIndex = families['reptile']
print(atIndex)

# Replace Value at Index
families["mammal"] = "Human Being"

# Add new items
families["cat"] = "Panther"

# Search by Key:
#
# NOTE: Membership is only checked on the keys.
isPresent = 'Present' if 'cat' in families else 'Absent'

# Don't throw the exception if Key is absent: Returns None
member = families.get('Pumpkin')

# Copying one Dictionary to an Existing Dictionary.
animals = families.copy()

# Alternative copy
creation = dict(families)

# Extend/Update a Dictionary with another Dictionary.
birds = dict(bird="Falcon")
creation.update(birds)


print(creation)

def main():
    createDictionary()

if __name__ == '__main__': main()