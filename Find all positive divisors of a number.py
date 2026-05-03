# Write a function to find all positive divisors of a number.
# Example:
# Input: 12
# Output: 123 4 6 12

num = int(input("Enter a Number: "))

def div_nums(n):
    divisors = []

    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

res = div_nums(num)
print(res)