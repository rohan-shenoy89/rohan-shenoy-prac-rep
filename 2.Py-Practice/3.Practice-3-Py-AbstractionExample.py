#-----------------------------
# PRACTICE - OOPS
# CORE SUBJECT - Abstraction
# DEVELOPER - Rohan Shenoy
#------------------------------

#Created a class with Name Car
class Car:

    def __init__(self):  #Calling the contructor without any values

        #Defined all the parameters as False
        self.acc = False
        self.clutch = False
        self.brk = False

    #Defined a Method for Car class
    def carStart(self):
        #Give are the parameters that are set to True and False
        # Abstraction - Object-oriented programming (OOP) abstraction is the process of hiding the implementation details of a class and showing only the necessary features of an object to the outside world
        self.acc = False
        self.brk = True
        self.clutch = True
        return "Car Started.."

car1 = Car() #Created an instance or Object and called the Car Class
print(car1.carStart()) # Called the 'carStart Method, It only returns the values in 'Return' statement, hiding other values that are set accordingly
