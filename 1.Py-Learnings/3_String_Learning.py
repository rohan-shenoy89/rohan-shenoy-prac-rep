#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - String Learing
#DEVELOPER - Rohan Shenoy
################################

#Exercise 1A: Create a string made of the first, middle and last character
#Write a program to create a new string made of an input string’s first, middle, and last character.

str = "James"

first = str[0]
middle = str[int(len(str)/2)]
last = str[-1]

print(first+middle+last)
print("\n*****************\n")

#Exercise 1B: Create a string made of the middle three characters
#Write a program to create a new string made of the middle three characters of an input string.

str = "JhonDipPeta"

mi = int(len(str)/2)
res = str[mi - 1:mi + 2]

print(res)
print("\n*****************\n")

#Exercise 2: Append new string in the middle of a given string

str1 = "Ault"
str2 = "Kelly"

mi = int(len(str1)/2)

res = str1[:mi:] + str2 + str1[mi:]
print(res)
print("\n*****************\n")

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

s1="America"
s2="Japan"

#Get the details of initial char
first = s1[0]+s2[0]

#Pull the len of the char or string and divide it by 2 to reach its middle point
mi1 = int(len(s1)/2)
mi2 = int(len(s2)/2)

#Take the above length as index and add them both
middle = s1[mi1]+s2[mi2]

#Get the details of last char
last = s1[-1]+s2[-1]

print(first+middle+last)
print("\n*****************\n")

#Exercise 5: Count all letters, digits, and special symbols from a given string

def countChar(str):
    charCount = 0
    alphaCount = 0
    symbolCount = 0

    for char in str:
        if char.isalpha():
            alphaCount += 1
        elif char.isdigit():
            charCount += 1
        else:
            symbolCount += 1
    print(f"The alphaCount: {alphaCount}")
    print(f"The charCount: {charCount}")
    print(f"the symbolCount: {symbolCount}")


countChar("P@#yn26at^&i5ve")
print("\n*****************\n")

#Exercise 6: Create a mixed String using the following rules

#def mixed(str1,str2):

str11 = 'Abc'
str21 = 'Xyz'
str31 = ''

str21 = str21[::-1]

length = len(str11)

for i in range(length):
    if i < length:
        str31 = str31 + str11[i]
    if i < length:
        str31 = str31 + str21[i]

print(str31)
print("\n*****************\n")

#Exercise 7: String characters balance Test

def check(str1,str2):
    Flag = True
    for i in str1:
        if i in str2:
            continue
        else:
            Flag = False
    return Flag

print(check('Py','Pynative'))
print("\n*****************\n")

#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

str="Welcome to USA. usa awesome, isn't it?"
findStr = 'USA'
tempStr = str.lower()
occurance = tempStr.count(findStr.lower())

print(f"The count of word USA: {occurance}")
print("\n*****************\n")


