#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - Data Structures Learing
#DEVELOPER - Rohan Shenoy
################################


#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd = []
even = []

for i in l1[1::2]:
    if i % 2 != 0:
        odd.append(i)
print("Element at odd-index positions from list one")
print(odd)
for j in l2[0::2]:
    if j % 2 == 0:
        even.append(j)
print("Element at even-index positions from list one")
print(even)
final = sorted(odd+even)
print(final)
print("\n*****************\n")

#Exercise 2: Remove and add item in a list

list1 = [54, 44, 27, 79, 91, 41]
print(list1)

list1.pop(4)
print("List after removing the index at 4: ",list1)

list1.insert(2,91)
print("List after adding the index at 2: ",list1)
print("\n*****************\n")

#Exercise 3: Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = int(len(sample_list)/3)
print(chunk_size)

start = 0
end = chunk_size

for i in range(chunk_size):
    indexes = slice(start, end)

    #Get the first chunk
    list1 = sample_list[indexes]
    print(list1)

    #reverse the order
    print("The reversed order of the list: ", list(reversed(list1)))
print("\n*****************\n")

#Exercise 4: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

counter_dict = dict()

for item in sample_list:
    if item in counter_dict:
        counter_dict[item] += 1
    else:
        counter_dict[item] = 1
print(f"{counter_dict}: ")
print("\n*****************\n")

#Exercise 5: Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print(first_list)
print("-----------------------------")
print(second_list)
print("-----------------------------")

result = zip(first_list,second_list)
print(list(result))
print("\n*****************\n")

#Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
result = list()

for item in roll_number:
    if item in sample_dict.values():
        result.append(item)
print(result)


#Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

set_val = set(speed.values())

result = list(set_val)
print(result)
print("\n*****************\n")

#Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_val = tuple(set(sample_list))
print(unique_val)

max = max(unique_val)
min = min(unique_val)
print("The max value: {0} and Min value: {1}".format(max,min))

