# Find maximum repeated character
# input: banana
# output: a

text = input("Enter a word: ")

max_char = ""
max_count = 0

for t in text:
    count = text.count(t)

    if count > max_count:
        max_count = count
        max_char = t

print(f"hello: {max_char}")