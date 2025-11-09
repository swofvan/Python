# Create a calculator program using OOPS. Make sure you create a class Calculator and
# then use its object to access the calculator operations such as addition,
# subtraction, division and multiplication.


class Calculator:

    def addition(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x - y
    
    def division(self, x, y):
        return x / y

    def multiplication(self, x, y):
        return x * y

calc = Calculator()

num1 = int(input("Enter a Number: "))

operation = input("Enter operation(+, -, *, /): ")

num2 = int(input("Enter a Number: "))

if operation == "+":
    print(f"{num1} + {num2} = {calc.addition(num1, num2)}")

elif operation == "-":
    print(f"{num1} - {num2} = {calc.subtraction(num1, num2)}")

elif operation == "*":
    print(f"{num1} x {num2} = {calc.multiplication(num1, num2)}")

elif operation == "/":
    print(f"{num1} / {num2} = {calc.division(num1, num2)}")

else:
    print("Invalid Operetion")