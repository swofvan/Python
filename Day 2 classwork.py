# You work for a bookstore that generates receipts for customers. Your task is to prepare a simple receipt using string techniques.
# Here’s what you need to do:
# Create a multiline string to store the receipt header.
# The customer bought 2 items:
# Book Title: "Python Basics" – ₹450
# Book Title: "Data Science Intro" – ₹600
# For each line showing the book and price, use a single string with basic {} placeholders and call format() once to fill in the values.
# Calculate the total price and add it similarly.
# Concatenate a thank-you message at the end.
# Make sure the output uses newline (\n) and tab (\t) for readability.
# Display the entire receipt in uppercase.

header = """\t Welcome to Bookstore
Date: October 13, 2025
Time: 12:50 PM IST"""

print(header.upper())

book1 = "Python Basics"
book2 = "Data Science Intro"

book1_price = 450
book2_price = 600

show =  "\nThe customer bought 2 items \n 1st book is {} - {} rs \n 2nd book is {} - {} rs"

print (show.format(book1,book1_price,book2,book2_price).upper())

total = book1_price + book2_price

total_text = "Total Price = {} + {} = {}"

print(total_text.format(book1_price,book2_price,total,).upper())

thank = "\n\tThank you"
meg = "For Choosing Us"

print(thank.upper(), meg.upper())