# Count letters in a sentence without spaces

text = input("Enter a Sentence: ")
txt = text.replace(" ", "")

count = len(txt)

print(count)