#Calculate the sum of all numbers from 1 to a given number

def calCum(n):

    s = 0
    for i in range(1, n+1):
        s += i
    print('')
    print(f"Sum is {s}")


n = int(input("Enter the number: "))
print(calCum(n))
