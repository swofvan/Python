# Fibonacci Program
# A Fibonacci series is a number pattern where:
# next number = previous two numbers added

# eg :  0, 1, 1, 2, 3, 5, 8, 13... ( 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8 )


num = int(input("Enter a num: "))

a = 0
b = 1

for i in range(num):
    print(a)
    
    c = a + b
    a = b
    b = c