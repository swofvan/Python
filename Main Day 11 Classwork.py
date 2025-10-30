# You are helping a travel blog store and manage recent trip details. 
# Each trip includes a city name, the date it was visited (in the format dd-mm-yyyy), and a short comment.
# 
# Your task is to:
# Create a Python module named tripdata.py with a function that returns trip details in dictionary format.
# In your main file, import the function and use it to build a list of trip dictionaries.
# For each trip:
#Convert the date string into a date object.
# Format the date to display as "Month Day, Year" (e.g., “May 15, 2023”).
# Convert the list of trip dictionaries to a JSON string and print it.

import json

from datetime import datetime
from tripdata import trip_details

trips = [
    trip_details("Paris", "15-05-2023", "France's capital"),
    trip_details("London", "20-08-2024", "capital of England and the United Kingdom"),
    trip_details("New York", "10-02-2025", "the perpetual heartbeat of America")
]

for t in trips:
   date_obj = datetime.strptime(t["Date"], "%d-%m-%Y")
   t["Date"] = date_obj.strftime("%B %d, %Y")

trips_json = json.dumps(trips, indent = 4)
print(trips_json)
