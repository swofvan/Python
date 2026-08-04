# Find Missing Number

nums = [1, 2, 3, 5, 7, 8]

missing_num = []

for n in range(nums[0], nums[-1]):
    if n not in nums:
        missing_num.append(n)

print(missing_num)