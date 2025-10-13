# A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
# The shop sold:
# 15.5 liters of apple juice
# 20 liters of orange juice
# 10.25 liters of grape juice
# Your task:
# Store the volume of each juice in separate variables.
# Calculate the total volume sold.
# Print the total volume.
# Convert the total volume to an integer and print it.
# Convert the total volume to a string and print it with a message.
# Add a random number between 5 and 10 (representing additional bonus liters) and print the final total

juice_1, juice_2, juice_3 = "apple", "orange",  "grape"
v_1, v_2, v_3 = 15.5, 20, 10.25
total = v_1 + v_2 + v_3

print('Total Volume = ', total)

int_total = int(total)
print ("Total to int = ", int_total)

total_string = str(total)
print ("Total Volume in String = " + total_string)

import random
bonus = random.randrange(5,10)
print("bonus liters = ", bonus)

print("Final Volume with bonus = ", total + bonus)