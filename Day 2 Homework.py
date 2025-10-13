# Write a Python program that does the following:
# Store a short paragraph about a Python course using a multiline string.
# Display the length of the paragraph (number of characters).
# Display the first and last characters in the paragraph.
# Slice and print a short preview: the first 50 characters.
# Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
# Convert the entire paragraph to lowercase.
# Remove any extra whitespaces from the start or end.
# Split the paragraph into individual words and print the list.
# Check if the word "course" exists in the paragraph. Print a message if found.
# Display the final message:
# "The course description is {} characters long and has {} words." using the format() method.

Py_course = """     A Python is a versatile, non-venomous snake known for its powerful
constricting ability, found in diverse habitats across Africa, Asia, and Australia.
In the context of programming, Python is a high-level, interpreted language
renowned for its simplicity and readability, making it ideal for beginners
and experts alike. Its extensive libraries support applications in web development,
data analysis, AI, and more, fostering a vibrant community of developers.
Whether slithering through jungles or powering modern software, Python embodies
adaptability and strength."""

py_len = len(Py_course)

print ("length = ",py_len)

print ("\nFirst = ", Py_course[0], ",  Last = ", Py_course[-1])

print ("\n",Py_course[:50])

py_replace = Py_course.replace("Python", "PYTHON")

print ("\n", py_replace)

print ("\n", Py_course.lower())

white_space = Py_course.strip()

print ("\n", white_space)

print ("\n", Py_course.split(" "))

print ("\n", "course" in Py_course)

msg = "\n The course description is {} characters long and has {} words."

print (msg.format(Py_course, py_len))