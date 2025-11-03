# Homework Problem:

# A local school wants to keep track of students' names in a file.
# Ask the user how many student names they want to add.
# Then, take that many names as input and store each name on a new line in a file called students.txt.
# If the file already exists, first show all existing names, then add the new ones without removing the old ones.
# After saving the new names, read and display the updated list of all student names.

num_of_students = int(input("Number of Students: "))

file = open ("students.txt", "a")

for num in range(num_of_students):
    name = input(f"Enter Name of Student: ")
    file.write(name + "\n")

file.close()

file = open ("students.txt", "r")
print(file.read())