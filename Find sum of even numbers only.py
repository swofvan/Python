# Find sum of even numbers only
# input: 10
# output: 30 (2 + 4 + 6 + 8 + 10)

num = ""

num = int(input("Enter a number: "))
even = []

for n in range(1, num + 1):
    if n % 2 == 0:
        even.append(n)

res = sum(even)

print(res)