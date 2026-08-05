# Count Frequency of Words
# Input: I love Python I love AI

# Output:
# I:2
# love:2
# Python:1
# AI:1

text = input("Enter a Sentence: ")

words = text.split()

result = {}

for w in words:
    if w in result:
        result[w] += 1
    else:
        result[w] = 1

print(result)