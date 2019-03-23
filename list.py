
from decorators import padding

# List
@padding
def shoppingList():
    shoppedItems = ["Ball","Iron","Grease","Carpet","Darts","Bat"]
    checkOut(shoppedItems)

def checkOut(collection):
    # Join Lists
    # NOTE: Using the concatenation operator doesn't modify the operands.
    newList = collection + ["Mangoe","Orange","Cucuber","Quava"]

    # Join using the "In-Place extension" i.e. +=
    # NOTE: Using the assigning Operand does modify the operands.
    newList += ["Gadamia","Melon"]

    # Alternatively
    newList.extend(["Pineapple", "Grape"])

    # Join using a Specific Separator
    separator = ', '.join(newList)
    print(separator)

    # Reverse a List
    reversedList = newList.reverse()
    print(reversedList)

    # Sorting in Descending Order
    numbersList = [29,30,7,12,111]
    numbersList.sort(reverse=True)   # [111, 30, 29, 12, 7]
    print(numbersList)

    # Sort in Place: i.e. Ascending order.
    numbers = [89,45,79,8]
    numbers.sort()
    print(numbers)

    # Order Based on some Key value. E.g. by len.
    #
    # The key Argument uses any callable object, which is then used to extract
    # the key from each item. Then the items will then be sorted relative to the
    # order of these keys.
    #
    # Hint; Read on "callable objects" in Python.
    newList.sort(key=len)
    print(newList)

    """ 
        reverse() 
            returns an iterator. which maybe not what you need.
            
        sort() 
            returns a new list which it then operates on.
    """

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

    # Shallow Copy a List into Another Independent new List.
    copiedList = newList[:]
    copiedList.append("Banana")

    # Repeating A List
    repeatedList = [['Borne','Baurne']] * 3
    print(repeatedList)

    print(copiedList)

    for item in newList: print(item, end=' ', flush=True)

def main():
    shoppingList()

if __name__ == '__main__': main()