# Write a program to display only those numbers from a list that satisfy the following conditions


def listNum(list):

#iterate over the list
    for i in list:
        if i > 500:
            break
        elif i > 150:
            continue
        # Check if the number is divided with 5
        elif i % 5 == 0:
            print(i)


list = [12, 75, 150, 180, 145, 525, 50]
print(listNum(list))

