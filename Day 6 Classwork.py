# You are working on a simple attendance tracking system for a 5-day workshop.
#                           You have a list of the number of students present each day:
# attendance = [18, 20, 19, 15, 21]
# Your tasks are:
# Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
# Count how many days the class was full.
# Calculate and print the total attendance for all 5 days.

attendance = [18, 20, 19, 15, 21]
print(attendance)

full_days = 0

for stu in attendance:
    if stu >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")

print("Full Days : ", full_days)

total_attendance = sum(attendance)
print("total_attendance : ", total_attendance)