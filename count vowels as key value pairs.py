# count vowels as key value pairs

text = input("Enter a Sentence: ").upper()

count = {}

vowels = "AEIOU"

for t in text:
    if t in vowels:
        count[t] = text.count(t)

print(count)