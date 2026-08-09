import random


while True:

    system_number = str(random.randrange(1000, 9999))

    user_input = input("Enter a 4 digit number: ")

    rabbits = []
    tortoise = []

    print(f"System number = {system_number}")

    if not user_input.isdigit() or len(user_input) != 4:
        print("invalid input")

    else:

        for n in range(4):
            if user_input[n] == system_number[n]:
                rabbits.append(n)

        for n in range(4):
            if user_input[n] in system_number and user_input[n] not in rabbits:
                tortoise.append(n)

        count_of_rabbit = len(rabbits)
        count_of_tortoise = len(tortoise)

        if user_input == system_number:
            print("Winner")

            continue_play = input(f"\n Do you want to continue? (y/n): ").lower

            if continue_play == "y":
                continue

            else:
                break

        print(f"you got {count_of_tortoise} tortoise")
        print(f"youb got {count_of_rabbit} rabbits")
