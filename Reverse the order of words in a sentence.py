# Reverse the order of words in a sentence

text = input("Enter a secntance: ");
words = text.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)

print(result)