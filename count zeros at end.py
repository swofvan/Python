# count 0 that comes end
# input = 100
# output = 2

num = input("Enter a number: ")

rev_num = num[::-1]
count = 0

for n in rev_num:
    if n == "0":
        count += 1
    else:
        break

print(count)