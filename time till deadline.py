# calculate time to deadline

import datetime

user_input = input("Enter Task with Deadline (Task:Deadline): ")
input_list = user_input.split(":")

task = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()

available_time = deadline_date - today_date

available_days = available_time.days

available_hours = int(available_time.total_seconds() / 60 / 60)

message_days = f"Dear user! Time remaining for \"{task}\" is \"{available_days}\" days"
message_hours = f"Dear user! Time remaining for \"{task}\" is \"{available_hours}\" hours"

print(message_days)
print(message_hours)