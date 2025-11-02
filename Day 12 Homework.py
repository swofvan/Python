# You are building a simple customer feedback system for a local restaurant.
# The system should ask users to enter their name and feedback.

# Your task is to:
# Ask the user to enter their name and feedback.
# If the user leaves the name or feedback empty, display an error message using exception handling.
# If all inputs are valid, print a thank-you message along with the user's name and feedback.
# Use the try, except, and finally blocks to structure your code safely.

import re

success = False

try:
    name = input("Enter Your Name: ")
    feedback = input("Enter Your feedback: ")

    if not re.match(r"[\S]", name):
        raise ValueError("Name Error: Please Enter your name")
    
    if not re.match(r"[\S]", feedback):
        raise ValueError("Feedback Error: Please Write Your Feedback")
    
    success = True
    
    print(f"\nName: {name}")
    print(f"Feedback: {feedback}")
    print("Thank you for your feedback")

except ValueError as error:
    print(error)

finally:
    if success:
        print("Feedback process completed.")
    else:
        print("Please try again")