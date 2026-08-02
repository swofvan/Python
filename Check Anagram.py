# Check Anagram
# input:
# listen
# silent

# Output:
# True


word_1 = input("Enter first word: ").lower()
word_2 = input("Enter second word: ").lower()

if sorted(word_1) == sorted(word_2):
    print("True")
else:
    print("False")