# Create a program for a mini library system that asks the user to enter a book title and publication year.
# If the book title contains only alphabets and spaces, accept it. Otherwise, show an error.
# The publication year must be a 4-digit number starting with “19” or “20”. If not, display an error.
# Use appropriate error handling to catch any invalid inputs and ensure a message is printed at the end whether or not there was an error.

import re

try:
    title = str(input("Book Title: "))
    year = input("Publication Year: ")

    if not re.fullmatch("[a-zA-Z\s]+", title):
        raise ValueError("TitleError: book title contains only alphabets and spaces.")
        
    if not re.fullmatch("(19|20)\d{2}", year):
         raise ValueError("Invalid Year: year must be a 4-digit number")
    
    print("Book added successfully!")
    print(f"Title: {title}")
    print(f"Publication Year: {year}")

except ValueError as error:
    print(error)