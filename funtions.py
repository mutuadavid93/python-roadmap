import random

# Must have the leading "def" keyword

def functionName(number1, number2 = 100):
    return number1+number2

sum = functionName(100)
print(sum)

def isPrime(n):
    return False if n % 2 == 0 else True

def listPrimes():
    for n in range(10):
        if isPrime(n):
            print(n, end=' ', flush=True)
    print()

listPrimes()

# Python Never Assumes Arguments if Required
# All Arguments with defaults must be at the end of Params' List.

# Argument lists: To pass unlimited arguments to a function
def argsList(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Default Sound is Purr')

# argsList("Grr","Meow","Yeow")
tupleOrListValues = ("Grr","Meow","Yeow") # or ["Grr","Meow","Yeow"]
argsList(*tupleOrListValues)

# Keyword "arguments" are dictionary args instead of list/tuple
def keywordArgs(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f"Key '{k}' has value '{kwargs[k]}'")
    else:
        print('Default value printed')

# keywordArgs(Ball = "Player", BallBoy="Kid")
dictionaryValue = dict(Ball = "Player", BallBoy="Kid")
keywordArgs(**dictionaryValue)


# Generator: A function which returns a stream of values
def genarator():
    my_list = [89,30,50,19]
    for i in my_list:
        yield i

for random_number in genarator():
    print('And the next number is %d '%(random_number))

# Decorator: A function that takes a function and returns a function.
# f1 below is a Decorator
def f1(f):
    def f2():
        print('before function call')
        f()
        print('after function call')
    return f2

# f1 decorator implicitly takes f3 function definition as an argument
# i.e.f1(f3) which is the "returned function reference" i.e. f2
# and reassigns it to f3 and on invoking f3() just works.
@f1
def f3():
    print('this is f3')

# returnedValue = f1(f3) # i.e. f2
# returnedValue()
f3()