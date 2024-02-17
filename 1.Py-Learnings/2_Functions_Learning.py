#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - String Learing
#DEVELOPER - Rohan Shenoy
################################

#Exercise 1: Create a function in Python
#Write a program to create a function that takes two arguments, name and age, and print their value.

def basic(name, age):
    print(f"The name is {name} and his age is {age}")


basic("Rohan",34)
print("\n*****************\n")


#Exercise 2: Create a function with variable length of arguments

def anyFunc(*args):
    for i in args:
        print(i)


anyFunc(10,20,30)
print("\n*****************\n")

#Exercise 3: Return multiple values from a function

def calculation(a, b):
    addition = a + b
    substraction = a - b
    return addition,substraction


res = calculation(40,10)
print(res)
print("\n*****************\n")

#Exercise 4: Create a function with a default argument
    #Write a program to create a function show_employee() using the following conditions.
    #It should accept the employee’s name and salary and display both.
    #If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print(f'The name is {name} and the salary is {salary}')


show_employee("Rohan",265000)
show_employee("Nishant")
print("\n*****************\n")

#Exercise 5: Create an inner function to calculate the addition in the following way
    #Create an outer function that will accept two parameters, a and b
    #Create an inner function inside an outer function that will calculate the addition of a and b
    #At last, an outer function will add 5 into addition and return it

def sum(a,b):
    add = 0
    def addition(a,b):
        return a + b
    add = addition(a, b)
    return add + 5

print(sum(40,10))
print("\n*****************\n")


#Exercise 6: Create a recursive function
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def recursive(num):
    if num:
        return num + recursive(num - 1)
    else:
        return 0

print(f'The sum of number is {recursive(10)}')
print("\n*****************\n")


#Exercise 7: Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)


display_student("Emma",20)

student_name = display_student
student_name("Emma",20)
print("\n*****************\n")

#Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def even_numbers(list):
    list = []
    for i in range(4,30,2):
        list.append(i)
    print(list)
    print()


print(even_numbers(list))
print("\n*****************\n")


#Exercise 9: Find the largest item from a given list

#def largest(max_val):
x = [4, 6, 8, 24, 12, 2]
max_val = x[0]

for num in x[1:]:
    if num > max_val:
        max_val = num
        print(max_val)

#print(largest())
