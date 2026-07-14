# Even and Odd Numbers

numbers = [1, 2, 3, 4, 5]

even_numbers = []
odd_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    elif n % 2 != 0:
        odd_numbers.append(n)
    else:
        pass


print(f"Odd Numbers: {odd_numbers}")
print(f"Even Numbers: {even_numbers}")