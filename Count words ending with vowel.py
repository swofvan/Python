# Count words ending with vowel

text = input("Enter a Sentance: ")

def count_vowels() :
    vowels = "AEIOUaeiou"
    count = 0

    t = text

    for p in '?.!,':
        t = t.replace(p, "")
    
    for w in t.split():
        if w[-1] in vowels:
            count += 1
    
    return count

print(count_vowels())