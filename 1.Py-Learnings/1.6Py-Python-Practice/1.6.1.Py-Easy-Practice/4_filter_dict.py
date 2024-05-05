# Filter dictionary to contain keys present in the given list

dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
lst = ['A', 'C', 'F']

keys = dict.keys()
new_dict = {}

if keys in lst:
    new_dict = dict.get(keys)
print(new_dict)
