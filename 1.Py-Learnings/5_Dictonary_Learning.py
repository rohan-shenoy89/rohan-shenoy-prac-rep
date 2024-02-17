#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - Dictonary Learing
#DEVELOPER - Rohan Shenoy
################################

#Exercise 1: Convert two lists into a dictionary

#Option 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys,values))
print(result)
print("\n*****************\n")

#Option 2
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict()

for i in range(len(keys)):
    result.update({keys[i]: values[i]})
print(result)
print("\n*****************\n")

#Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

result = dict1.copy()
result.update(dict2)

print(result)
print("\n*****************\n")

#Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "classes": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


#Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees,defaults)
print(result)
print("\n*****************\n")

#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_Dict = dict()

for k in keys:
    new_Dict = {k: sample_dict[k]}
    print(new_Dict)
print("\n*****************\n")

#Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
print("\n*****************\n")

#Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
findVal = 200

if findVal in sample_dict.values():
    print("{0} is present in a dict".format(findVal))
else:
    print("{0} is not present in a dict".format(findVal))
print("\n*****************\n")

#Exercise 8: Rename key of a dictionary

#Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

l = "location"
sample_dict[l] = sample_dict.pop("city")
print(sample_dict)

#Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict.values()))


sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)
