import random

system_number = str(random.randrange(1000, 9999))

user_input = input("Enter a 4 digit number: ")


print(f"System number = {system_number}")

if user_input.isalpha or len(user_input) != 4:
    print("invalid input")

else:
    if user_input == system_number:
        print("Winner")