def palindrome(i):
    i = str(i)
    return i == i[::-1]


i = '123'
if palindrome(i):
    print("Is Palindrome")
else:
    print("Is not Palindrome")
