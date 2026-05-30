# Find all factors of a number
# input: 10
# output: [1, 2, 5, 10]


num = int(input("Enter a number: "))

factors = []

for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)

print(factors)