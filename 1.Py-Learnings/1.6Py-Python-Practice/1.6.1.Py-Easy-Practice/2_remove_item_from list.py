#Remove items from a list while iterating


# In this question, You need to remove items from a list while iterating but without creating a different copy of a list.
# Remove numbers greater than 50

def removeItem(num_list):

    i = 0
    n = len(num_list)
    print(n)
    while i < n:
        if num_list[i] > 50:
            del num_list[i]
            n = n - 1
        else:
            i = i + 1
    return num_list

num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(removeItem(num_list))
