from decorators import padding

@padding
def createDictionary():
    creatures = {"Human": "Mammal", "Alligator": "Reptile", "HornBill": "Bird"}

    # Alternative Definition
    crops = dict(citrus="Orange", vegetable="Amaranthus")

    # Keys Must always be Immutables: e.g. Strings and Integers
    humans = {45 : "Ball", "KSH": 45000}

    display_dict(creatures)
    keyCommaValue(crops)

def display_dict(animals):
    for animal in animals: print('%s : %s' %(animal,animals[animal]))

def keyCommaValue(collection):
    # Print Key and Value
    for key, value in collection.items():
        print(f'Key : {key} and Value: {value}')

    # Print Only The Keys
    for key in collection.keys(): print(key)

    # Print only The Values
    for value in collection.values(): print(value)

    # Get value at Specific index
    atIndex = collection['citrus']
    print(atIndex)

    # Replace Value at Index
    collection["citrus"] = "Lemon"

    # Add new items
    collection["thorned"] = "Cactus"

    # Search by Key
    inCollection = 'Present ' if 'thorned' in collection else 'Absent'

    # Don't throw the exception if Key is absent: Returns None
    member = collection.get('Pumpkin')

    print(member)

def main():
    createDictionary()

if __name__ == '__main__': main()