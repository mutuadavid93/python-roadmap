"""
    Model for Aircraft

    __init__(self):
            An instance method for initialiazing new objects.


    Law Of Demeter:
        Never allow a class (i.e. Target e.g. Aircraft) Method/Attribute be
        accessed directly from another class (i.e. Source e.g. Flight).

        Instead pass the "Target" class reference through the "Source"
        class __init__() then use it.
"""

from pprint import pprint as pp

class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        self._number =number
        self._aircraft = aircraft

        # tuple unpacking: (range(1, 23), 'ABCDEF')
        rows, seats = self._aircraft.seating_plan()

        # [None], Waste the first row index to start rows at index 1.
        # By joining with the list comprehensions which has a sub-dictionary comprehension.
        #
        # Requirement : 2 Rows and 2 Seats Per Row === 4 Seats.
        # Logic: (range(1, 3), 'AB')
        #
        # Result, [None,{A: None, B: None},{A: None, B: None}]
        #
        # _ means we discard row variable.
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]


    def number(self):
        return self._number

    def airline(self):
        return self._number[:3]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """Pass a seat designator into a valid row and letter

            Args:
                seat: A seat designator such as '21E'

            Returns:
                A tuple containing an Integer and a String for row and letter
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError('Invalid row number {}'.format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

            Args:
                seat: A seat designator e.g. '10C' or '23F'.
                passenger: The passenger's name.

            Raises:
                ValueError: if the seat is unavailable
        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} is already occupied.'.format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

            Args:
                from_seat: existing seat designator for the passenger to be moved.

                to_seat: New seat designator.
        """

        from_row, from_letter = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate to seat {}.'.format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat {} is occupied.'.format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

        return self._seating


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows+1), 'ABCDEFGHJK'[:self._num_seats_per_row])



"""Polymorphism.

    Definition:
        Using objects of different types ( i.e. Constructed using different classes)
        through a common/uniform interface.
        
    Example:
        The two planes below AirbusA390 and Boeing737.
        
        Notice they have no any relationship to each other or to any class in 
        our Hierarchy. But have similar Interface.
"""
class AirbusA390:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A390"

    def seating_plan(self):
        return (range(1, 23), 'ABCDE')

class Boeing737:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing MAX737"

    def seating_plan(self):
        return (range(1, 56), 'ABCDEFJK')



# Construct a Plane:
plane = Aircraft('Q-TYU', 'Boeing Qatar', num_rows=22, num_seats_per_row=5)

plan = plane.seating_plan()  # returns a tuple: (range(1, 23), 'ABCDEF')



"""Implementation Details Zone:"""

def make_flights():
    flight = Flight('ANU890', AirbusA390('BXZ780'))

    # Booking Seats
    flight.allocate_seat('12A', 'Lonzo Ball')
    flight.allocate_seat('1E', 'Jose Ingram')
    flight.allocate_seat('03B', 'Khris Dunn')
    flight.allocate_seat('01C', 'Kyle Kuzma')
    flight.allocate_seat('01B', 'Zaza Pachulia')
    flight.allocate_seat('01A', 'Lebron James')

    worl_flight = Flight('ANU891', AirbusA390('XCV751'))

    # Booking Seats
    worl_flight.allocate_seat('12A', 'Tyron Lanester')
    worl_flight.allocate_seat('1E', 'Kings Slayer')
    worl_flight.allocate_seat('03B', 'Karisi Denerys')
    worl_flight.allocate_seat('01C', 'John Snow')
    worl_flight.allocate_seat('01B', 'Lord Stack')
    worl_flight.allocate_seat('01A', 'Arya Stack')

    return flight, worl_flight

# Move Lonzo Next to Ingram
f, g = make_flights()
updated_seating = g.relocate_passenger('12A', '1D')

plane_model = f.aircraft_model()

pp(updated_seating)