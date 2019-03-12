class MyClass:
    aproperty = "A Class Property"

    def aFunction(self):
        print("A statement from a function")

myobject1 = MyClass()
myobject2 = MyClass()

# Each object contains independent copies of the variables defined in the class.
myobject2.aproperty = "Ball City"

print(myobject1.aproperty)      # "A Class Property"
print(myobject2.aproperty)      # "Ball City"

myobject1.aFunction()