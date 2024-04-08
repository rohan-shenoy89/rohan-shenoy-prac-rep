#Python Array

# Write a Python program to find the maximum element in an array

def find_max(arr):
    max_vl = arr[0]

    for i in arr:
        if i > max_vl:
            max_vl = i
    return max_vl

# Test the function
arr = [5, 3, 9, 1, 7]
print("Maximum element:", find_max(arr))


# Calculate the Sum of All Elements in an Array:

def cal_sum(arr):

    sum_val = 0

    for i in arr:
        sum_val += i

    return sum_val


arr = [5, 3, 9, 1, 7]
print("Sum element:", cal_sum(arr))


# Find the Average of All Elements in an Array:

def find_avg(arr):

    avg_val = 0
    sum_val = 0

    for i in arr:
        sum_val += i

        avg_val = sum_val/len(arr)
    return avg_val

arr = [5, 3, 9, 1, 7]
print("Avg element:", find_avg(arr))


# Count the Number of Even Numbers in an Array:

def count_even(arr):

    cnt_even = 0

    for i in arr:
        if i % 2 == 0:
            cnt_even += 1

    return cnt_even

# Test the function
arr = [5, 3, 9, 1, 7, 8, 10, 2]
print("Number of even numbers:", count_even(arr))

# Remove Duplicates from an Array:

def remove_dup(arr):

    unique_dt = []
    dup_dt = []

    for i in arr:
        if i in unique_dt:
            dup_dt.append(i)
        else:
            unique_dt.append(i)
    return dup_dt


# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
print("Array with duplicates removed:", remove_dup(arr))

# Get second highest number from array

def sec_high(arr):

    max_val = arr[0]
    sec_max = 0

    for i in arr:
        if i > max_val:
            sec_max = max_val
            max_val = i
        elif i > sec_max and i < max_val:
            sec_max = i
    return sec_max


arr = [5, 3, 9, 1, 7, 8, 10, 2]
print("Second Highest number in the list:", sec_high(arr))

# Get third highest number from array

def third_high(arr):

    max_val = arr[0]
    sec_high = arr[0]
    third_high = 0

    for i in arr:
        if i > max_val:
            third_high = sec_high
            sec_high = max_val
            max_val = i
        elif i > sec_high:
            third_high = sec_high
            sec_high = i
        elif i > third_high:
            third_high = i
    return third_high


arr = [5, 3, 9, 1, 7, 8, 10, 2]
print("Third Highest number in the list:", third_high(arr))
