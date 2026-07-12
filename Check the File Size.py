# Check the File Size

import os

file = os.stat('students.txt')

print(file.st_size)