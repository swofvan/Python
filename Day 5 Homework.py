# You are managing an online course portal that keeps track of student enrollments
#                                            in two subjects: "Frontend" and "Backend".
# Create two sets:
# One with the names of students enrolled in the Frontend course
# One with the names of students enrolled in the Backend course
# Perform the following tasks:
# Add a new student to the Backend course
# Remove a student from the Frontend course
# Display the list of students who are enrolled in both courses
# Display the list of students who are enrolled only in Backend, but not in Frontend
# Display the total number of unique students
# Create a dictionary where:
# Keys are course names ("Frontend", "Backend")
# Values are the number of students enrolled in each
# Print each course name with the number of students using a loop
# Using dictionary comprehension, create a new dictionary that adds a
#                                    "Fullstack" course by combining student counts from both existing courses.


Frontend = {"Jishnu", "Lakshmi", "Sree", "Fabisha"}
Backend = {"Swofvan", "Akhila", "Lakshmi", "Nikhil"}

print("Frontent : ", Frontend)
print("Backend : ", Backend)

Backend.add("Bibin")
print("Backend : ", Backend)

Frontend.remove("Fabisha")
print("Frontend : ", Frontend)

print(Frontend.intersection(Backend))

print(Backend - Frontend)

total_stu = Backend.union(Frontend)
print("Total students : ", len(total_stu))

dictionary = {
    "Frontend" : len(Frontend),
    "Backend" : len(Backend)
}

for stu in dictionary:
    print("courses : ", stu, "\nStudents : ", dictionary[stu])

new_dictionary = {course: x for course, x in dictionary.items()}
print(new_dictionary)

new_dictionary["Fullstack"] = dictionary.get("Frontend") + dictionary.get("Backend")
print(new_dictionary)