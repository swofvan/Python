# Print Palindrome words with function


text = input("Enter a Sentence: ")
words = text.split()

palindrome = []

def check_palindrome():
    for w in words:
        if w == w[::-1]:
            palindrome.append(w)

check_palindrome()

print(palindrome)