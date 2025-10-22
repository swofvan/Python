# you are creating a basic system to manage students enrolled in various courses.
# Create two sets: one for students enrolled in "Python" and one for "Data Science".
# Add a new student to the Python set.
# Remove one student from the Data Science set.
# Find and display the names of students who are enrolled in both courses.
# Find students who are only in the Python course but not in Data Science.
# Display the combined list of all students in either course (no duplicates).
# Create a dictionary with course names as keys and number of students as values.
# Using a loop, print the course name and number of students in the format:
# Course: Python, Students: 3
# Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)

Python = {"Nikhil", "Swofvan", "Lakshmi","Bibin", "Sonu"} 
Data_Science = {"Bibin", "Sonu", "Rohan", "Kuriakos"}

Python.add("Akhila")
print(Python)

Data_Science.remove("Rohan")
print(Data_Science)

print(Python.intersection(Data_Science))

print(Python - Data_Science)

print(Python.union(Data_Science))

num_of_stu = {
    "Python" : len(Python),
    "Data Science" : len(Data_Science)
}
print(num_of_stu)

for course in num_of_stu:
    print("Course : ", course, "\nStudent : ", num_of_stu[course])

dict_comp = {course: stu * 2 for course, stu in num_of_stu.items()}
print(dict_comp)