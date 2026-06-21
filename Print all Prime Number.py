# Print all Prime Numbers in an Interval

lower = int(input("Enter Starting Number: "))
upper = int(input("Enter Ending Number: "))


for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)