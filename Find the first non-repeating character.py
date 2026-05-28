# Find the first non-repeating character
# input: "aabbcde"
# output: "c"


text = input("Enter a word: ")

for ch in text:
    if text.count(ch) == 1:
        print(ch)
        break