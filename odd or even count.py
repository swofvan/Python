# odd or even count

numbers = input("Enter a list of numbers coma suparated(,): ")

number_list = numbers.split(",")

num_dict = {
    "odd" : 0,
    "even" : 0,
}

for num in number_list:
    if num.strip().isalpha():
        print("Please add numbers only")

    else:

        n = int(num)

        if n % 2 == 0:
            num_dict["even"] += 1

        else:
            num_dict["odd"] += 1

print(num_dict)