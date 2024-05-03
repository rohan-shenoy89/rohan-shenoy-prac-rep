#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - List Learing
#DEVELOPER - Rohan Shenoy
################################

#Exercise 1: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]

list1 = list1[::-1]
print(list1)

#Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = list()

for i, j in zip(list1,list2):
    result.append(i+j)
print((result))

#Exercise 3: Turn every item of a list into its square

number = [1,2,3,4,5,6,7]
result = list()
for i in number:
    result.append(i * 2)
print(result)


pet = {'color': 'red', 'age': 42}

for i in pet.item():
    print(i)
