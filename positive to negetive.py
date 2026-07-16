# input = [1,-2, 3, -4, 5]
# output = [1, 3, 5, -2, -4]

nums = [1,-2, 3, -4, 5 ]

p_num = []
n_num = []

for n in nums:
    if n < 1:
        n_num.append(n)
    if n >= 1:
        p_num.append(n)

out = p_num + n_num

print(out)