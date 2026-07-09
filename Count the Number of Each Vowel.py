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
    if t == "a":
        count["a"] += 1
    elif t == "e":
        count["e"] += 1
    elif t == "i":
        count["i"] += 1
    elif t == "o":
        count["o"] += 1
    elif t == "u":
        count["u"] += 1

print(count)    