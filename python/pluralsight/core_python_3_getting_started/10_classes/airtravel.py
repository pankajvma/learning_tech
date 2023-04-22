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
            raise ValueError(f"No passsanger to relocate in seat {to_seat}.")
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied.")
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
    
class Aircraft:

    def __init__(self, registration, model,  num_rows, num_seats_per_row):
        self._registration  = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])
    
# Convenience method
def make_flight():
    flight = Flight('BA758', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
    flight.allocate_seat('12A', 'Guido van Rossum')
    flight.allocate_seat('15F', 'Bjarne Stroustrup')
    flight.allocate_seat('15E', 'Anders, Hajlsberg')
    flight.allocate_seat('1C', 'John McCarthy')
    flight.allocate_seat('1D', 'Rich Hickey')

    return flight
    
