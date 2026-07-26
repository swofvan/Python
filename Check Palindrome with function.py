# Check Palindrome with function

text = input("Enter a Word: ")

def check_palindrome() :
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome()