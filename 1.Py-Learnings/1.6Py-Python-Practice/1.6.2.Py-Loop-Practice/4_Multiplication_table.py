# Write a program to print multiplication table of a given number

def multiplication(n):

    for i in range(1,11):
        result = n * i
        print(f" {n} * {i} = {result}")


n = 3
print(multiplication(n))
