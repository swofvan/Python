# You are creating a mini lucky draw system for a small online gift store.

# Ask the user to enter names of customers (comma-separated) who have placed orders today.
# Remove any duplicate names from the list.
# Randomly shuffle the final list of names.
# Pick and display 2 winners using random selection.
# For fun, reverse the names of both winners before displaying.
# Display the total number of unique participants.
# Use the math module to show the square root of the number of participants, rounded to the nearest whole number.

import random
import math

customers = input("Enter Customer Names(comma-separated): ")
customers_list = customers.split(",")
print(f"Customers: {customers_list}")


unique_customers = []
[unique_customers.append(x) for x in customers_list if x not in unique_customers]
print(f"Unique customers: {unique_customers}")

random.shuffle(unique_customers)
print(f"Shuffled: {unique_customers}")

winners = random.choices(unique_customers, k = 2)
# winners_str = str(winners)
reversed_winners = [name [::-1] for name in winners]
print(f"reversed_winners: {reversed_winners}")

total_unique_participants = len(unique_customers)
print(f"total unique participants: {total_unique_participants}")

square_root = math.sqrt(total_unique_participants)
rounded_num = math.ceil(square_root)
print(f"Rounded square root: {rounded_num}")