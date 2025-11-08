# Consider the following array
# [{id:1, name:"rajesh"}, {id:2, name: "rahul"}, {id:3, name: "sruthi"}]
# Write a program to accept a number and print the name of the student with that id

employee = [
    {"id":1, "name":"rajesh"},
    {"id":2, "name":"rahul"},
    {"id":3, "name":"sruthi"}
]

num = int(input("Enter Employee id: "))
em_id = False

for i in employee:
    if i["id"] == num:
        print(f"Employee ID:{i["id"]} , Name: {i["name"]}")
        em_id = True
        break

if not em_id:
    print("Wrong Employee ID")