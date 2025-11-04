# You are helping to create a simple name game for a birthday event.

# Ask the user to enter a list of names of invited guests (comma-separated).
# Remove any duplicate names.
# Randomly choose one name from the final list to play a game.
# Reverse the selected name and display it.
# Also, print the total number of unique names and round the square root of that number to the nearest whole number.

import random
import math
 
guests = input("Enter Name of Guests (comma-separated): ")
name_list = guests.split(",")
print (name_list)

uniqe_names = []

for x in name_list:
    if x not in uniqe_names:
        uniqe_names.append(x)

print(str(uniqe_names))

random_name = random.choice(uniqe_names)
print(f"Random Name: {random_name}")

reversed_name = random_name [::-1]
print(f"Reversed Name: {reversed_name}")

total_uniqe_names = len(uniqe_names)
print(f"Total Uniqe Names: {total_uniqe_names}")

square_root = math.sqrt(total_uniqe_names)
print(f"Squere root: {square_root}")