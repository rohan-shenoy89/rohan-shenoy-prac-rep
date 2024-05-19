# Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def empDetails(name,salary=9000):
    print(f"Name: {name} and Salary: {salary}")


result = empDetails("Ben", 12000)
result2 = empDetails("Jessca")
