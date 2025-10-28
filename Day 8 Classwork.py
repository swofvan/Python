# A company wants to create a simple system to define and display employee profiles based on their
# role types for record-keeping purposes. You are tasked with creating classes to represent different
# types of individuals in Python. Complete the following steps:

# Create a class Person with attributes name (string) and age (integer), and a method
# show_details() that prints the person’s name and age.

# Create a class Employee that inherits from Person,
# adds an attribute employee_id (string), 
# and includes a show_details() method to print the employee’s name, age, and employee ID.

# Create a class PartTime that inherits from Person,
# adds an attribute working_hours (float), and
# includes a show_details() method to print the part-time worker’s name, age, and working hours.

# Create a class Consultant that inherits from both Employee and PartTime,adds an attribute project_name (string),
# and includes a show_details() method to print the consultant’s name, age, employee ID, working hours, and project name.

# Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
# Display the details of each object by calling its show_details() method


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
            print("Name: ",self.name,",  Age: ", self.age)

p1 = person("Swofvan", 22)
p1.show_details()

# ========================================================================================== 

class employee(person):
    def __init__(self, name, age, employee_id):
          person.__init__(self,name, age)
          self.employee_id = employee_id
    
    def show_details(self):
        print("Name: ", self.name, ",   Age: ", self.age, ",   Employee ID: ", self.employee_id)

employee_1 = employee("Akhila", 23, "MS002")
employee_1.show_details()

# ===========================================================================================

class PartTime(person):
     def __init__(self, name, age, working_hours):
          super().__init__(name, age)
          self.working_hours = working_hours

     def show_details(self):
          print("Name: ", self.name, ",   Age: ", self.age, ",   Working houres: ", self.working_hours,"hours")

PartTime_1 = PartTime("Lakshmi", 24, 5.30)
PartTime_1.show_details()

# =============================================================================================

class Consultant(employee, PartTime):
     def __init__(self, name, age, employee_id, working_hours, project_name):
          employee.__init__(self, name, age, employee_id)
          PartTime.__init__(self,name,age ,working_hours)
          self.project_name = project_name

     def show_details(self):
          print("\nName: ", self.name, "\nAge: ", self.age, "\nEmployee ID: ", self.employee_id, "\nWorking houres: ", self.working_hours," hours,", "\nProject: ", self.project_name)

Consultant_1 = Consultant("Nikhil", 21, "MS003", 8.00, "Mashup Stack")

Consultant_1.show_details()