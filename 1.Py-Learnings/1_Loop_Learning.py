#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - Loop Learing
#DEVELOPER - Rohan Shenoy
################################

#Exercise 1: Print First 10 natural numbers using while loop

for i in range(1,11):
    print(i)
print("\n*****************\n")


#Exercise 2: Print the following pattern

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print("\n*****************\n")

#Exercise 3: Calculate the sum of all numbers from 1 to a given number

number = 10
sum = 0

for i in range(1, number+1):
    sum += i
print(f"The Entered Number: {number}")
print(f'Sum: {sum}')
print("\n*****************\n")

#Exercise 4: Write a program to print multiplication table of a given number

result = 0
number = 2

for i in range(1,12):
    if result > 0:
        print(result)
    result = i * number
print("\n*****************\n")


#Exercise 5: Display numbers from a list using loop
#Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
print("\n*****************\n")


#Exercise 6: Count the total number of digits in a number
#Write a program to count the total number of digits in a number using a while loop.

number = 123456
counter = 0

while number != 0:
    number = number // 10
    counter += 1
print(counter)
print("\n*****************\n")

#Exercise 7: Print the following pattern

n = 5
k = 5

for i in range(0, n + 1):
    for j in range(k-i,0,-1):
        print(j, end = ' ')
    print()
print("\n*****************\n")

#Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
list1 = list1[::-1]

for i in list1:
    print(i)
print("\n*****************\n")

#Exercise 9: Display numbers from -10 to -1 using for loop

for i in range(-10,0):
    print(i)
print("\n*****************\n")

#Exercise 10: Use else block to display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
else:
    print("Done!")
print("\n*****************\n")

#Exercise 11: Write a program to display all prime numbers within a range

start = 25
end = 50

for num in range(start, end+1):
    if num > 0:
        for i in range(2,num):
            if num % 2 == 0:
                break
        else:
            print(num)
print("\n*****************\n")


#Exercise 12: Display Fibonacci series up to 10 terms

number = 10
result = 0

a, b = 0, 1
for i in range(1, number + 1):
    print(a, end=' ')
    result = a+b

    a = b
    b = result
print("\n*****************\n")

#Exercise 12: Display Fibonacci series up to 10 terms

number = 5
factorial = 1

if number < 0:
    print("The Factorial of negative is not available")
elif number == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial = factorial * i
    print(factorial)
print("\n*****************\n")

#Exercise 14: Reverse a given integer number

integers = 76542

#THIS IS PENDING TO BE DONE

#Exercise 15: Use a loop to display elements from a given list present at odd index positions

my_list = [10,20,30,40,50,60,70,80,90,100]

for i in my_list[1::2]:
    print(i,end=' ')
print("\n*****************\n")

#Exercise 16: Calculate the cube of all numbers from 1 to a given number

number = 6

for i in range(1,number+1):
    if i > 6:
        break
    else:
        print(f"The number is {i} and its cube is {i ** 3}")
