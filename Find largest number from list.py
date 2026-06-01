# Find largest number from list

num = [10, 20, 15, 60, 45]

largest = num[0]

for n in num:
    if n > largest:
        largest = n

print(largest)