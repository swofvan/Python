# Find Duplicate Numbers

nums = [1,2,3,2,4,5,1]

seen = []
dupe = []

for n in nums:
    if n in seen and n not in dupe:
        dupe.append(n)
    seen.append(n)

print(dupe)