# Reverse the order of words in a sentence
# input: I love You
# output: You Love I

text = input("Enter a secntance: ");
words = text.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)

print(result)