def add_passenger(seats, seat_class, passenger_name):
    """
    Adds a passenger to the first available seat in the correct section.
    First 10 seats are for 'Business' Class.
    Next 10 seats are for 'First' Class.
    The remaining seats are for 'Economy' Class.
    """
    if seat_class == 'Business':
        seat_range = range(0, 10)
    elif seat_class == 'First':
        seat_range = range(10, 20)
    elif seat_class == 'Economy':
        seat_range = range(20, len(seats))

    for s in seat_range:
        if seats[s] is None:
            seats[s] = passenger_name
            return True
    return False


aircraft_seats = [None] * 100   # creates list of None of length 100

add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "First", "Bob")

print(aircraft_seats[:15])  # Expected output: ['Alice', 'Eve', None, None, None, None, None, None, None, None, 'Bob', None, None, None, None]

"""
To complete this exercise:
--------------------------
The aircraft seating is divided into Business Class (first 10 seats), First Class (next 10 seats), 
and Economy Class (remaining seats).
We use the `None` value to represent empty seats.


Exercise Breakdown:
-------------------
To find the first available seat, use the `is None` to check if the seat is free.
"""
