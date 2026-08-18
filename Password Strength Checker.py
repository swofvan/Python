# Password Strength Checker

password = input("Enter your password: ")

upper_case = False
lower_case = False

special_characters =  "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
is_sp_char = False

number = False

for ch in password:
    if ch.isupper():
        upper_case = True
        
    if ch.islower():
        lower_case = True

    if ch in special_characters:
        is_sp_char = True
        
    if ch.isdigit():
        print("num: ", ch)
        number = True
 
if len(password) >= 8 and upper_case and lower_case and is_sp_char and number:
    print("Password Valid")

else:
    print("Invalid Password")

    if len(password) < 8:
        print("Password must need at least 8 characters")
    if not upper_case:
        print("Password must need least one uppercase character")
    if not lower_case:
        print("Password must need least one lowercase character")
    if not is_sp_char:
        print("Password must need least one special characters")
    if not number:
        print("Password must need least one digit")