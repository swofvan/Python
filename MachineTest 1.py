# Write a program to print N rows in the following pattern
# *
# **
# ***

num = int(input("Enter a Number: "))

for x in range(num + 1):
    for y in range(x):
       print("*", end="")
    print("")