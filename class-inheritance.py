
"""
    Syntax:
        class ChildClass(ParentClass1, ParentClass2)

    Just take care of the Member Names so they Don't Clash.
"""

class Employee:
     def __init__(self, name):
       self._name = name

     def __str__(self):
         return "Eployee object default description overwritten."

     def get_name(self):
         return self._name.upper()



class Person:
    pass

    def get_identity_card(self):
        return "ID number : 30096789"


class Lawyer(Employee, Person):
    pass

    # Method Overriding : Override Parent's Method
    #
    # Polymorphism: Similar Method's Signature exists both in parent
    # and child Classes, e.g. get_name(), but the "implementation form maybe
    # different" in the child class.

    def get_name(self):
        original_name = super().get_name()
        print("Magistrate")
        return original_name

advocate = Lawyer("Joane")
employee = Employee("Strawman")

# Method from another Parent Class: Person
id_card = advocate.get_identity_card()


# NB: If the child class object is used to call an overriden method,
# then the child's overriden method is called. i.e.
joane = advocate.get_name()

# NB: If the parent class object is used to call an overriden method,
# then the parent's overriden method is called. i.e.
strawman = employee.get_name()

print("Employee: {} and {}".format(joane, id_card))
print(employee)