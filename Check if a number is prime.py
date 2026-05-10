# Check whether a number is prime or not.

num = int(input("Enter a number: "))

is_prime = True

for x in range(2,num):
    if num % 2:
        is_prime = False
        break

print(is_prime)