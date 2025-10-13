# A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
# Rice: ?45 per kg
# Sugar: ?40 per kg
# Oil: ?130 per kg
# Assume a customer bought:
# 3 kg of rice
# 2.5 kg of sugar
# 1.8 kg of oil
# Your task:
# Use variables to store the prices and quantities.
# Use appropriate data types.
# Calculate and print the total price for each item and the final total bill.
# Show the total bill as an integer and also as a string.
# Convert the float values where needed using explicit conversion.
# Use random number generation to add a random ?5–?10 delivery charge.
# Show the final bill amount including delivery charge.

p1 = "rice"
p2 = "sugar"
p3 = "oil"

p1_rs = 45
p2_rs = 40
p3_rs = 130

p1_q = 3
p2_q = 2.5
p3_q = 1.8

p1_total = p1_rs * p1_q
p2_total = p2_rs * p2_q
p3_total = p3_rs * p3_q

print(p1, p1_q, "kg = ",p1_total, "rs")
print(p2, p2_q, "kg = ",p2_total, "rs")
print(p3, p3_q, "kg = ", p3_total, "rs")

bill = p1_total + p2_total + p3_total

print("Total bill =", bill, "rs")
print(type(bill))

bill_int = int(bill)
print(bill_int)
print(type(bill_int))

bill_str = str(bill)
print(bill_str)
print(type(bill_str))

import random
delivery_charge = random.randrange(5,10)
print("Delivery Charge = ", delivery_charge,"rs")

final_bill = bill + delivery_charge
print("Final Bill = ", final_bill, "rs")