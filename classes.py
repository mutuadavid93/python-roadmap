class MyClass:
    aproperty = "class property"

    def aFunction(self):
        print("A statement from a function")
        print(f'A class method accesses a {self.aproperty}')

myobject1 = MyClass()
myobject2 = MyClass()

# Each object contains independent copies of the variables defined in the class.
myobject2.aproperty = "Ball City"

# Accessing class attributes
myobject1.aproperty     # "A Class Property"
myobject2.aproperty     # "Ball City"

myobject1.aFunction()