# Display Fibonacci series up to 10 terms

a = 0
b = 1

for i in range(10):
    print(a)
    res = a + b

    a = b
    b = res

