# Find the longest word in a sentence
# input: "Find the longest"
# output: "longest"

text = input("Enter a Sentence: ")
words = text.split()

longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print(longest)