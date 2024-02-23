#*******************************
#   SUBJECT - Python Learning
#   CORE SUBJECT - PYTHON CHEATSHEET
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


egg = 'Rohan'
spam()
print(egg)

#######################
# Python Lists
######################

#Getting values with indexes
furniture = ['table', 'chair', 'rack', 'shelf']

print(furniture[0])
print(furniture[1])
print(furniture[-1])
print(furniture[:-1])
print("\n*****************\n")

#Getting sublists with Slices
furniture = ['table', 'chair', 'rack', 'shelf']

print(furniture[0:4])
print(furniture[1:4])
print("\n*****************\n")

# Slicing complete list to copy
spam=['cat', 'bat', 'rat', 'elephant']

spam2 = spam[:]
print(spam2)

spam.append('dog')
print(spam)
print("\n*****************\n")

#Changing values with indexes

furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'

print(furniture)

furniture[2] = furniture[1]
print(furniture)
print("\n*****************\n")

#Getting the index in a loop with enumerate()

furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):
    print(f"The index at {index} is item {item}")
print("\n*****************\n")

#Loop in Multiple Lists with zip()

furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture,price):
    print(f" The item {item} is of ${amount}")
print("\n*****************\n")

# The in and not in operators
print('rack' in furniture)
print('bed' in furniture)
print("\n*****************\n")

# The index Method

furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture.index('chair'))
print("\n*****************\n")

# Adding Values
# append
furniture = ['table', 'chair', 'rack', 'shelf']

furniture.append('bed')
print(furniture)

# insert
furniture.insert(2,'sofa')
print(furniture)
print("\n*****************\n")

#Removing Values
#remove

furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture.remove('rack'))
print("\n*****************\n")

#pop
animals = ['cat', 'bat', 'rat', 'elephant']
animals.pop()

print(animals)

animals.pop(0)
print(animals)
print("\n*****************\n")

#Sorting values with sort()
numbers = [2, 5, 3.14, 1, -7]

numbers.sort()
print(numbers)

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()

print(furniture)
print("\n*****************\n")

#reverse the list
furniture.sort(reverse=True)
print(furniture)
print("\n*****************\n")

letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
print(letters)
print("\n*****************\n")

#Using the sorted function

furniture = ['table', 'chair', 'rack', 'shelf']
result = sorted(furniture)
print(result)
print("\n*****************\n")

##################
# Python Dictionaries
##################

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

#Set key, value

my_cat['age_year'] = 2
print(my_cat)
print("\n*****************\n")

#Get value using subscript operator []

print(my_cat['size'])
print("\n*****************\n")

#values()

pet = {'color': 'red', 'age': 42}

for i in pet.values():
    print(i)
print("\n*****************\n")

#keys()

pet = {'color': 'red', 'age': 42}

for i in pet.keys():
    print(i)
print("\n*****************\n")

#item()

pet = {'color': 'red', 'age': 42}
for i in pet.items():
    print(i)
print("\n*****************\n")

#get()

wife = {'name': 'Rose', 'age': 33}

print(f"My wife name is {wife.get('name')}")
print(f"She is {wife.get('age')} old")
print("\n*****************\n")

#Adding items with setdefault()

wife = {'name': 'Rose', 'age': 33}

if 'has_hair' not in wife:
    wife['has_hair'] = True

# Using the setdefault makes the code more small and easy

wife.setdefault('has_hair', True)
print(wife)
print("\n*****************\n")

#Removing Items
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.pop('age')

print(wife)
print("\n*****************\n")

#popitem()
wife.popitem()
print(wife)
print("\n*****************\n")

#del()
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}

del wife['age']

print(wife)
print("\n*****************\n")

#clear()

wife.clear()
print(wife)
print("\n*****************\n")

#Checking keys in a Dictionary

person = {'name': 'Rose', 'age': 33}

result = 'name' in person.keys()
print(result)
print("\n*****************\n")

#Checking values in a Dictionary

person = {'name': 'Rose', 'age': 33}

result = 'Rose' in person.values()
print(result)
print("\n*****************\n")

#Merge two dictionaries

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

result = {**dict_a, **dict_b}
print(result)
print("\n*****************\n")

#################
# Set
#################

#Initializing a set

s = {} #option one to create a set
s1 = set()
print(type(s))
print(type(s1))
print("\n*****************\n")

#Unordered collections of unique elements

s = {1, 2, 3, 2, 3, 4}
print(s)
print("\n*****************\n")

#set add() and update()

#Using the add() method we can add a single element to the set.

s = {4,5,6}
s.add(7)

print(s)
print("\n*****************\n")

#And with update(), multiple ones:

s.update([8,9,10])
print(s)
print("\n*****************\n")

#set remove() and discard()

#Both methods will remove an element from the set, but remove() will raise a key error if the value doesn’t exist

s.remove(10)
print(s)
print("\n*****************\n")

#discard will not raise any execptions

s.discard(10)
print(s)
print("\n*****************\n")

#set union()

s1 = {1, 2, 3}
s2 = {3, 4, 5}

result = s1.union(s2)
print(result)
print("\n*****************\n")

#set intersection

#intersection or & will return a set with only the elements that are common to all of them.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

result = s1.intersection(s2,s3)           #Intersect can be done like this too - s1 & s2 & s3
print(result)
print("\n*****************\n")

#set difference
#difference or - will return only the elements that are unique to the first set (invoked set).

s1 = {1, 2, 3}
s2 = {2, 3, 4}

result = s1.difference(s2)
print(result)
print("\n*****************\n")


#set symetric_difference
s1 = {1, 2, 3}
s2 = {2, 3, 4}

result = s1.symmetric_difference(s2)
print(result)
print("\n*****************\n")


########################
# Python Comprehensions
########################

# List comprehension vs basic coding

#basic
names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = list()

for n in names:
    new_list.append(n)
print(new_list)

#comprehension

new_list = [n for n in names]
print(new_list)
print("\n*****************\n")

#Adding conditionals

# Basic

new_list2 = list()

for n in names:
    if n.startswith('C'):
        new_list2.append(n)
        print(new_list2)
print("\n*****************\n")

# Comprehension

new_list2 = [n for n in names if n.startswith('C')]
print(new_list2)
print("\n*****************\n")

# To use an if-else statement in a List Comprehension:

# basic
nums = [1, 2, 3, 4, 5, 6]

for n in nums:
    if n % 2 == 0:
        print(n*2)
    else:
        print(n)
print("\n*****************\n")

# Comprehensions

new_list = [n*2 if n % 2 == 0 else n for n in nums]
print(new_list)
print("\n*****************\n")


########################
# Manipulating Strings
########################

# Escape characters

print("Hello there!\nHow are you?\nI\'m doing fine.")
print("\n*****************\n")

#Raw strings

#A raw string entirely ignores all escape characters and prints any backslash that appears in the string.

print(r"Hello there!\nHow are you?\nI\'m doing fine.")
print("\n*****************\n")

#Indexing and Slicing strings

# Indexing

spam = "Hello World"

print(spam[0])
print(spam[1])
print(spam[-1])
print("\n*****************\n")

# Slicing

spam = "Hello World!"

print(spam[0:5])
