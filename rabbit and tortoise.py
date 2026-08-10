import random

def system_number():
    system_number = str(random.randrange(1000, 9999))
    return system_number

sys_num = system_number() 

while True:

    user_input = input("\nEnter a 4 digit number: ")

    rabbits = []
    tortoise = []

    print(f"\nSystem number = {sys_num}\n")


    if not user_input.isdigit() or len(user_input) != 4:
        print("invalid input")

    else:

        for n in range(4):
            if user_input[n] == sys_num[n]:
                rabbits.append(user_input[n])

        for n in range(4):
            if user_input[n] in sys_num and user_input[n] not in rabbits:
                tortoise.append(user_input[n])

        count_of_rabbit = len(rabbits)
        count_of_tortoise = len(tortoise)

        if user_input == sys_num:
            print("Winner")

            
        print(f"you got {count_of_tortoise} tortoise")
        print(f"youb got {count_of_rabbit} rabbits")
