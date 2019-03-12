# Get the Length of a String
length = len('Horizontal')

print("String length is {}".format(length))

# Get Index of a Specific Character
# Based on first occurence from index 0
phrase = "Mattinez"
characterIndex = phrase.index('t')

print('Letter "L" at Index {}'.format(characterIndex))

# Slice a String
# @Syntax: astring[start:end]
astring = "Frustration"
diced = astring[1:5]

print("End index minus 1 gives the word '{}'".format(diced))

# Keep start and the colon
secondString = 'Second'
toTheEnd = secondString[2:]

print('Prints to the end of string, that is "{}"'.format(toTheEnd))

# Keep the Colon and End
anotherString = 'Another'
toThatIndex = anotherString[:4]

print('Prints upto that index, that is "{}"'.format(toThatIndex))

# Negatives means begin from the end
yetAString = "Lognabrothrok"
fromEnd = yetAString[-5:]

print("Prints from the end of string, that is '{}'".format(fromEnd))

# Reverse a String
fourthString = 'Maryland'
endStart = fourthString[::-1]

print('Reverses a string that is, "{}" becomes "{}"'.format(fourthString,endStart))

# If a string starts with something or ends with something, respectively.
theString = "Hello Folks"
startsWith = theString.startswith('Hello')
endsWith = theString.endswith('Folks')

print("'{}' starts with 'Hello': {}".format(theString, startsWith))
print("'{}' Ends with 'Folks': {}".format(theString, endsWith))

# Split a String into bunches stashed into a list
splitString = "Yo Guys"
splitted = splitString.split(" ")

print('"{}" split into a list: "{}"'.format(splitString, splitted))

# Converting a String into an Integer
rawString = "100"
numberValue = 100
castedStringToNumber = int(rawString)

print(castedStringToNumber == numberValue) # True

