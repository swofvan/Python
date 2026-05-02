# Count Words Ending with a Vowel Write a function that
# counts how many words in a sentence end with a vowel (a, e, i, o, u).
# Ignore punctuation. Treat uppercase and lowercase vowels the same.
# Input: "Are we going to see a movie?"
# Output: 6 (Words: "Are", "we", "to", "see", "a", "movie")

text = input("Enter Something: ")

def count_vowels(sentence):

    vowels = "aeiouAEIOU"
    count = 0

    for pun in ".,?!":
        sentence = sentence.replace(pun,"")
    
    word = sentence.split()

    for w in word:
        if w[-1] in vowels:
            count += 1

    return count

result = count_vowels(text)
print("count: ", result)