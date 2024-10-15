import time
import random

def time_me(func):
    """
    Return the number of milliseconds it took to execute the func function.
    Since execution time may vary from time to time, execute func 10 times and return the average running time.
    """
    total_time = 0

    # Run the function 10 times
    for _ in range(10):
        start_time = time.time()  # Get the start time in seconds
        func()  # Execute the function
        end_time = time.time()  # Get the end time in seconds

        # Calculate the time difference in milliseconds and accumulate
        total_time += (end_time - start_time) * 1000  # Convert to milliseconds

    # Calculate the average time
    average_time = total_time / 10

    return average_time

time_took = time_me(lambda: time.sleep(2 + random.random()))
print(time_took)  # Prints the average time in milliseconds


"""
To complete this exercise:
--------------------------
Implement the 'time_me' function to measure the average execution time of a given function over 10 runs.


Exercise Breakdown:
-------------------
The `time` module provides various time-related functions.
`time.time()` returns the current time in seconds since the Epoch. 
By calculating the difference between the start and end times, you can measure how long a function takes to execute.
"""
