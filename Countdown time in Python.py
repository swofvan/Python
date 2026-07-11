# Countdown time in Python

import time

time_input = int(input("Enter Time in seconds: "))

def count_down(seconds):
    while seconds > 0:
        minutes = seconds // 60         # Calculates the number of complete minutes
        remaining_seconds = seconds % 60        

        print(f"{minutes:02d}:{remaining_seconds:02d}", end="\r")  # Displays the time in MM:SS format on the same line.

        time.sleep(1)

        seconds -= 1

        print("00:00")
        print("Time is up")

count_down(time_input)