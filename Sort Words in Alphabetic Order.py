# Sort Words in Alphabetic Order

text = input("Enter a Sentance: ")

words = text.split()

for w in range(len(words)):
    words[w] = words[w].lower()

words.sort()

for w in words:
    print(w)