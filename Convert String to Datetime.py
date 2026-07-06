# Python Program to Convert String to Datetime

from datetime import datetime

my_date_string = "Dec 01 2026 11:31AM"

date_time_obj = datetime.strptime(
    my_date_string, '%b %d %Y %I:%M%p')

print(date_time_obj)
print(type(date_time_obj))

