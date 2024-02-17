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
