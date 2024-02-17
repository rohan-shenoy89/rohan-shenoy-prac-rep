#################################
#SUBJECT - Python Learnig
#CORE SUBJECT - Loop Learing
#DEVELOPER - Rohan Shenoy
################################

#Function to Calculate Factorial:

def factorial(n):
    result = 1 # Define initial value in result argument

    for i in range(1, n+1): #For loop to iterate over the given range
        result += i         # Add each number to the result from above given range
    return result           # Return the result


print(f"The value for given Factorial - {factorial(11)}")        # Call the function to get the result
print("\n*****************\n")

#Function to Check for Palindrome

def palindrome(word):
    word = word.lower()     # Make sure the all the letters are in lower case

    for s in range(len(word)//2): # Take the length of the word and round it up with base
       if word[s] != word[-s -1]: # Check if 1st letter is not eq to last letter
           return False           # if yes, return False
    return True                   # Else return True


palindrome('Radar')               # Take the value in the function:
if True:                          # Check the functions returned value and print your statement
    print(f"The given word is a Palindrome")
else:
    print(f"The given word is not a Palindrome")
print("\n*****************\n")

