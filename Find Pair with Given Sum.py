# Find Pair with Given Sum
# Input:
# [3,7,1,9]

# Target = 10

# Output:
# (3,7)
# (1,9)


num = [3,7,1,9]
target = 10

result = []

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] + num[j] == target:
            result.append((num[i], num[j]))

print(result)
