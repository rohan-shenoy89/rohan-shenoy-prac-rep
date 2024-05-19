# Create a recursive function
    # Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0


result = addition(10)

print(result)

