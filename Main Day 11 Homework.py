# You are building a simple activity tracker for a travel blog.Each time a traveler visits a place,
# the system stores the city name, a visit comment, and the visit date in the format "dd-mm-yyyy".

# Your task is to:
# Create a module called tracker.py that contains a function to return a travel record (as a dictionary).
# In the main file, use the function to create a list of at least 3 travel records.
# Convert the date string of each record into a readable format like "Month Day, Year" (e.g., "June 05, 2022").
# Convert the list of records into a JSON string and print it.
# Parse the JSON back to a Python object and display each record on a separate line.

import json

from tracker import travel_record
from datetime import datetime

record_list = [
    travel_record("Paris", "France's capital", "13-03-2025"),
    travel_record("London", "capital of England and the United Kingdom", "20-08-2024"),
    travel_record("New York", "the perpetual heartbeat of America", "10-02-2025")
]

for record in record_list:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

tracker_json = json.dumps(record_list, indent = 4)
print(tracker_json)
