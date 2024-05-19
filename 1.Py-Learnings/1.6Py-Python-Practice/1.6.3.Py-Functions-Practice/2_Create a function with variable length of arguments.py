#  Write a program to create function func1() to accept a variable length of arguments and print their value.

def percentage(*args):
    for i in args:
        print(i)


print("Printing Values")
result = percentage(20, 40, 60)
print(result,end=' ')

print("Printing Values")
result2 = percentage(10,30)
print(result2)
