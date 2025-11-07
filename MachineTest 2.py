# Write a program to enter a number and print its multiplication table till 10 rows.

num = int(input("Enter a Number: "))

for x in range(1, 11):
    print(f"{x} x {num} = {num * x}")