# Print multiplication table

num = int(input("Enter a Number: "))

for i in range(1, 11):
    res = num * i
    print(f"{num} * {i} = {res}")