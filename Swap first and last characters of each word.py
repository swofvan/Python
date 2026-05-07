# Swap First and Last Characters of Each Word Write a function that swaps the first
# and last character of each word in a sentence. Assume each word has at least one character.
# Input: "code test case"
# Output: "eodc tets ease"

text = input("Enter a sentance:")

def swap(sen):
    words = sen.split()
    new_words = []

    for w in words:
        if len(w) == 1:
            new_words.append(w)

        else:
            new_word = w[-1] + w[1:-1] + w[0]
            new_words.append(new_word)

    return " ".join(new_words)

res = swap(text)
print(res) 