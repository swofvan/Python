# Factorial of a Number using Loop

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist in Negetive Number")

elif num == 0:
    print(1)

else:
    for i in range(1, num+1):
        factorial *= i

    print(factorial)
