# A fitness center wants to create a simple system to define and display staff profiles based on
# their roles for record-keeping purposes. You are tasked with creating a Python program to represent
# different types of staff. Complete the following steps:

# Define a base class Employee with attributes name (string) and role (string), and a method display()
# that prints the employee’s name and role.

# Create a class Trainer that inherits from Employee, adds an attribute specialization (string),
# and includes a display() method to print the trainer’s name, role, and specialization.

# Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string),
# and includes a display() method to print the yoga instructor’s name, role, and yoga style.

# Create a class MultiTrainer that inherits from both Trainer and YogaInstructor,
# includes both specialization and yoga_style attributes, and has a display() method to print the
# multi-trainer’s name, role, specialization, and yoga style.

# Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
# Display the details of each object by calling its display() method


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Employee: ", self.name,",  Role: ",self.role)

employee_1 = Employee("Swofvan","Trainer")
employee_1.display()

# ----------------------------------------------------------------

class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print("Employee: ", self.name,",  Role: ",self.role, ",  specialization: ",self.specialization)

employee_2 = Trainer("Swofvan", "Trainer" , "Sports nutrition")
employee_2.display()

# ----------------------------------------------------------------

class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Employee: ", self.name,",  Role: ",self.role, ",  Yoga Style: ",self.yoga_style)

employee_3 = YogaInstructor("Jishnu", "Yoga Trainer" , "Hatha")
employee_3.display()

class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        YogaInstructor.__init__(self, name, role, yoga_style)

    def display(self):
        print("Employee: ", self.name,",  Role: ",self.role, "specialization: ", self.specialization , ",  Yoga Style: ", self.yoga_style)

employee_4 = MultiTrainer("Bibin","Multi Trainer", "strength", "Ashtanga") 
employee_4.display()