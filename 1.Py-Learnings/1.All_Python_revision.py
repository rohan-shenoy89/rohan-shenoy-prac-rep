#*******************************
#   SUBJECT - Python Learning
#   CORE SUBJECT - Loop Learning
#   DEVELOPER - Rohan Shenoy
#*******************************

#********************
# BASIC
#********************

greeting = "Hello "
greeting += "World"

print(greeting)
print("\n*****************\n")

my_list = ['Item']
my_list *= 3

print(my_list)
print("\n*****************\n")

# Warlus Operator

print(my_var:= "Hello Rohan")
print("\n*****************\n")

# Concatenation and Replication

# Concatenation
print('Alice' 'Rohan') #Not there is just a space to concat
print("\n*****************\n")

# Replication

print('Rohan ' * 5)
print("\n*****************\n")

# Variables
# Good Variable

var = "Hello "
print(var)
print("\n*****************\n")

# Bad Variable
#my var = "Rohan"

# unuseful variable

_spam = "World"
print(_spam)
print("\n*****************\n")

# The print() Function

a = 10
print("Hello World",a)
print("\n*****************\n")

# The end keyword

phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']

for i in phrase:
    print(i, end = ' ')
print("\n*****************\n")

# The sep keyword

print('cats', 'dogs', 'mice', sep=',')
print("\n*****************\n")

#The input() Function

print("What is your name?")
#my_name = input()
#print("Hi {}, welcome".format(my_name))


#********************
# CONTROL FLOW
#********************

#Operator #Meaning
#==	Equal to
#!=	Not equal to
#<	Less than
#>	Greater Than
#<=	Less than or Equal to
#>=	Greater than or Equal to

print(42 == 42)
print("\n*****************\n")

print(40 == 42)
print("\n*****************\n")

print("hello" == "hello")
print("\n*****************\n")

#Boolean operator

#The and Operator’s Truth Table:
#
#Expression	Evaluates to
#True and True	True
#True and False	False
#False and True	False
#False and False	False
#The or Operator’s Truth Table:

#Expression	Evaluates to
#True or True	True
#True or False	True
#False or True	True
#False or False	False

# Function Arguments

def say_hi(name):
    print(f"Hello {name}")

say_hi("Rohan")
print("\n*****************\n")

# Keyword Arguments
def say_hi(name, greeting):
    print(f"Hi {name}, {greeting}")

say_hi(name="Rohan", greeting="How are you?")
print("\n*****************\n")

# Return Values

def sum(num1, num2):
    return num1+num2

print(sum(10,20))
print("\n*****************\n")

#Local and Global Scope

global_variable = "I am global"

def inner(var):
    print(global_variable)
    local_variable = "I am local variable"
    print(local_variable)

print(global_variable)
print("\n*****************\n")

# The global Statement

def spam():
    global egg
    egg = 'spam'

#egg = 'Rohan'
spam
