# collect 2 input numbers from users
# print numbers between them
# skip even numbers
# if numbers from multiplication table of 10. stop printing


num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))


for i in range(num_1, num_2 + 1):
    
    if i % 10 == 0:
        break
    
    elif i % 2 == 0:
        continue

    else:
        print(i)
