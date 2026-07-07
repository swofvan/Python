# Remove Punctuations From a String

text = input("Enter a Sentance: ")

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text_without_punctuations = ""

for txt in text:
    if txt not in punctuations:
        text_without_punctuations += txt

print(text_without_punctuations)