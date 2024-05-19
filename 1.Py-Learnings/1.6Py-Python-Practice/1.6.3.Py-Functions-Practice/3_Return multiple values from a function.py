# Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

def calculation(a,b):
    add = a + b
    sub = a - b
    return add, sub


print(calculation(40, 10))


