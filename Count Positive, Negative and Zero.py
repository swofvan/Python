# Count Positive, Negative and Zero

# Input:
# [-1,0,2,-5,6]

# Output:
# Positive = 2
# Negative = 2
# Zero = 1


nums = [-1,0,2,-5,6]

positive = 0
negative = 0
zero = 0

for n in nums:
    if n > 0:
        positive += 1
    elif n == 0:
        zero += 1
    elif n < 0:
        negative += 1

print(f"Positive = {positive}\nNegative = {negative}\nZero = {zero}")