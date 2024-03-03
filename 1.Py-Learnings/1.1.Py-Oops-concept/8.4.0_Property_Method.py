# Property Method

class Student:

    def __init__(self, name, phy, chem, maths):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths)/3) + '%' # Even after the marks are changed, the value of percentage will not change

        # Rather there are 2 options to dynamically change the values of percentage
        # Option 1 - Define a method

    def calcPercentage(self):
        print(str((self.phy + self.chem + self.maths)/3) + '%')


        # Option 2 - Using the property method
    @property
    def calcPercentage2(self):
        return str((self.phy + self.chem + self.maths)/3) + '%'

stud1 = Student("Rohan Shenoy", 98, 97, 90)
print(stud1.percentage)

stud1.phy = 80
print(stud1.calcPercentage())

stud1.phy = 89
print(stud1.calcPercentage2)
# Note - If you are using the @prroperty method, you need to only call the object name as attribute

