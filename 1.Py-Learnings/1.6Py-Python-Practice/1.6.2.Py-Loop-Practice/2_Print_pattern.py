# Write a program to print the following number pattern using a loop

def pattern():

    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=' ')



print(pattern())
