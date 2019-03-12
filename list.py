
from decorators import padding

# List
@padding
def shoppingList():
    shoppedItems = ["Ball","Iron","Grease","Carpet","Darts","Bat"]
    checkOut(shoppedItems)

def checkOut(collection):
    # Join Lists
    newList = collection + ["Mangoe","Orange","Cucuber","Quava"]

    # Join using a Specific Separator
    separator = ', '.join(newList)
    print(separator)

    # Start at Index 1 and Stop at Sixth Item Stepping on Every Second Item.
    print(newList[1:6:2])

    # Add Items
    newList.insert(0,"Golf")

    # Remove item by value
    newList.remove("Bat")

    # Remove Item from a Specific Index
    newList.pop(newList.index('Golf'))

    # Remove an Item By Index using Delete
    del newList[5]

    # Remove by a Slice: Begin removing items
    # from index 2 upto to fith item and other items in step of two simultaneously
    del newList[2:5:2]

    # Get the List Length
    print(len(newList))

    for item in newList: print(item, end=' ', flush=True)

def main():
    shoppingList()

if __name__ == '__main__': main()