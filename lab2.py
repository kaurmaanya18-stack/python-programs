name = input("Enter Employee Name: ")
print("Data type:", type(name))

emp_id = int(input("Enter Employee ID: "))
print("Data type:", type(emp_id))

salary = float(input("Enter Salary: "))
print("Data type:", type(salary))

dept = input("Enter Department: ")
print("Data type:", type(dept))

active_input = input("Is the employee active? (yes/no): ")
if active_input == "yes":
    active = True
else:
    active = False
print("Data type:", type(active))

print("")
print("--- Employee Details ---")
print("Name       :", name)
print("ID         :", emp_id)
print("Salary     :", salary)
print("Department :", dept)
print("Active     :", active)
