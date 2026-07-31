# Find Intersection of Lists

nums_1 = [1,2,3,4,5]
nums_2 = [2,4,6,8,10]

result = []

for i in nums_1:
    if i in nums_2:
        result.append(i)

print(result)