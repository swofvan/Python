# input = [2, 8, 5, 6, 4]
# target = 10
# output = [(2,8), (6,4)]
# 2+8 = 10

nums = [2, 8, 5, 6, 4]

target = 10

result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result.append((nums[i], nums[j]))

print(result)