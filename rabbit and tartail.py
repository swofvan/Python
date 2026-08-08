import random

system_number = str(random.randrange(1000, 9999))

user_input = input("Enter a 4 digit number: ")

rabbits = []
turtles = []

print(f"System number = {system_number}")

if not user_input.isdigit() or len(user_input) != 4:
    print("invalid input")

else:
    if user_input == system_number:
        print("Winner")

    for n in range(4):
        if user_input[n] == system_number[n]:
            rabbits.append(n)

    for n in range(4):
        if user_input[n] in system_number and user_input[n] not in rabbits:
            turtles.append(n)

    print(f"you got {len(turtles)} turtles")
    print(f"youb got {len(rabbits)} rabbits")