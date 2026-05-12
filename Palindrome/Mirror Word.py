# Check whether a string is palindrome (mirror word).

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")