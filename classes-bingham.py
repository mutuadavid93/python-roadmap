# Convention: Class Names use CamelCase in Python 3.+

"""A Comment"""

"""
    Simplest Possible Class needs at least a Do nothing 'pass' 
    statement to be Syntactically admisible 
"""

"""
    Instance methods - Functions which can be called on objects
"""

"""
    self - the first argument to all instance methods
"""

"""
    initializer: Instance method for initializing new objects.
    
    NB: __init__() is an initializer, NOT a constructor
"""

"""
    constructor - Provided by the runtime system to check the 
    existence of an instance initializer and call it if present.
"""

class Flight:
    pass

    def __init__(self, flight_number, aicraft):
        self._number = flight_number
        self.validator(self._number)
        self._aicraft = aicraft

    def get_number(self):
        return self._number

    def get_airline(self):
        return self._number[:3].upper()

    def get_aircraft_model(self):
        return self._aicraft.get_model()

    def validator(self, flight_number):
        if not flight_number[:3].isalpha():
            raise ValueError("First three characters must be alphabets")

        if not flight_number[3:].isdigit():
            raise ValueError("The last airline code part must be a number")




class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def get_model(self):
        return self._model

    def get_registration(self):
        return self._registration

    def count_passengers(self):
        total_seats = self._num_rows * self._num_seats_per_row
        return total_seats


""" 
    NB: Passed in Key Value pairs e.g. num_rows=157 
    for documentation purpose.
"""
plane = Aircraft("737BJ", model="BOENG", num_rows=17, num_seats_per_row=9)

plane_model = plane.get_model()
passengers_role = plane.count_passengers()

print('%d passengers onboard.' % (passengers_role))



""" __init__() args must be passed into the class constructor """
flight = Flight("yth78", Aircraft("890XJ",model="SKELDAR",num_rows=5,num_seats_per_row=2))


""" Invoking class methods """

"""
    @Way1:
"""
flight_number1 = flight.get_number()

"""
    @Way2: Not popular
"""
flight_number2 = Flight.get_number(flight)
flight_airline = flight.get_airline()

# LoD applied:
"""
    Law of Demeter:
    Never call Methods on objects received from  other calls.

    Layman's; Only talk to your friends.

    Hint: There should be no Intermediaries
    @Example;
    Instead of obj.getX().getY().getZ().get_model()
    Do: obj.get_model()
"""
aircraft_model = flight.get_aircraft_model()
print(aircraft_model)