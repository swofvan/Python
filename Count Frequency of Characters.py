# Count Frequency of Characters

# Input: banana

# Output:
# {
# 'a':3,
# 'b':1,
# 'n':2
# }

word = input("Enter a Word: ")

result = {}

for w in word:
    if w in result:
        result[w] += 1
    else:
        result[w] = 1

print(result)
