"""Model for aircraft flights"""

class Flight:

    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        # class invariant
        # check if the entered flight number is valid. A valid flight number starts with 2 alphabets followed by 4 digit number.
        if not number[:2].isalpha():  
            raise ValueError(f"No airline code in {number}")
        
        if not number[:2].isupper():  
            raise ValueError(f"Invalid airline code  {number}")
        
        if not(number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number  '{number}'")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
        
    
    def number(self):
        return self._number, '5'
    
    
    def airline(self):
        return self._number[2:]
    
    def print_seating(self):
        count = 0
        seperator_len = 11 * len(self._seating[1])
        seperator = '='* seperator_len
        print(seperator)
        for rows  in self._seating[1:]:
            count+=1
            for seat, passenger in rows.items():
                if passenger is None:
                    print(f'{count}{seat}: {passenger}', end = '')
                    if list(rows)[-1] != seat:
                        print(', ', end = '')
                else:
                    if seat != 'A' and self._seating[count][chr(ord(seat)-1)] is None:
                        print()
                    print(f'{count}{seat}: {passenger}', end = '')
                    if list(rows)[-1] != seat:
                        print(', ')
            print()
            print(seperator)

    
    # We have used '_' in the beginning because this function is an implementation detail and should not be called directly from outside the class.
    # Rememember unlike Java, We dont have Access modifiers in python so we use different naming conventions to signify how an agtribute/function should be used.
    def _parse_seat(self, seat): 
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]  # Extract last character
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1]  # Extract row number by excluding last charater

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row  {row_text}")
        
        if row not in rows:
            raise ValueError(f"Invalid seat row  {row}")
        
        return row, letter
    

    def allocate_seat(self, seat, passanger):
        """Allocate a seat to a passanger.
        
        Args:
            seat: A seat designator such as '12c' or '12F'.
            
        Raises: 
            ValueError: If the seat is unavailable.    
        """
        row, letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")
        
        self._seating[row][letter] = passanger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate passanger to a different seat.
        
        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passsanger to relocate in seat {from_seat}.")
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied.")
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        # available_seats = 0
        # for row in self._seating[1:]:
        #     available_seats += list(row.values()).count(None)
        # return available_seats

        # OR we can use the below approach mentioned in the course
        return sum(sum(1 for v in row.values() if v is None) 
                   for row in self._seating 
                   if row is not None)
    
    # This function accepts another function to print boarding cards.
    # This mthod can accept any function of the specified format. However, We will use console_card_printer().
    # Polymorphism: Using objects of different types thorugh a uniform interface. In python it applies to both functions as well  as more complex types.
    # Polymorphism in python is achieved through Duck-Typing.
    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):     # This is a generator funtion
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")
    
class Aircraft:

    def __init__(self, registration):
        self._registration  = registration

    def registration(self):
        return self._registration
    
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)
    
# Creating seperate aircrafts and demonstrating inheritance.
class AirbusA319(Aircraft):
    
    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1, 23), "ABCDEF"
    

class Boeing777(Aircraft):
    
    def model(self):
        return "Boeing777"
    
    def seating_plan(self):
        return range(1, 56), "ABCDEFGH"
    
# New requirement: Method to print boarding passes
# This method is built on the principle of "Tell! Don't Ask."
# Notice that how the function below doesn't knwo anything about flights or aircrafts. It's very loosely coupled.
def console_card_printer(passanger, seat, flight_number, aircraft):
    output = f"| Name: {passanger}"     \
        f"  Flight: {flight_number}"    \
        f"  Seat: {seat}"               \
        f"  Aircraft: {aircraft}"       \
        "   |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

# Convenience method
def make_flights():
    flight1 = Flight('BA758', AirbusA319('G-EUPT'))
    flight1.allocate_seat('12A', 'Guido van Rossum')
    flight1.allocate_seat('15F', 'Bjarne Stroustrup')
    flight1.allocate_seat('15E', 'Anders, Hajlsberg')
    flight1.allocate_seat('1C', 'John McCarthy')
    flight1.allocate_seat('1D', 'Rich Hickey')

    flight2 = Flight('AF72', Boeing777('F-GSPS'))
    flight2.allocate_seat('55G', 'Larry Wall')
    flight2.allocate_seat('33G', 'Yukihiro Matsumoto')
    flight2.allocate_seat('4B', 'Brian Kernihan')
    flight2.allocate_seat('4A', 'Dennis Ritchie')

    return flight1, flight2
    

# test input
# from airtravel import *
# aircraft1 = AirbusA319('G-EUPT')
# aircraft2 = Boeing777('F-GSPS')
# aircraft1.num_seats()
# aircraft2.num_seats()
# f, g = make_flights()
# f.print_seating()
# f.num_available_seats()
# f.make_boarding_cards(console_card_printer)
