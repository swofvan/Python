# Count uppercase and lowercase letters
#   Eg: HelloWorld
#   Uppercase: 2
#   Lowercase: 8


text = input("Enter a Sentence: ")

upper = 0
lower = 0

for t in text:
    if t.isupper():
        upper += 1
    elif t.islower():
        lower += 1

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")