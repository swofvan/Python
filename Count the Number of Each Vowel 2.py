# Count the Number of Each Vowel

text = input("Enter Input :")

text_lower = text.lower()

count = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}


for t in text_lower:
    if t in count:
        count[t] += 1 

print(count)