class Student():
    college = "PGMCOE" #Class Attribute
    name = "Anynonomus"

    def __init__(self,name,marks):
        self.name = name #Object Attribute
        self.marks = marks


    def getAvg(self):
        result = (sum(self.marks)/3)
        print(f"Hi {self.name} you percentage is {result}%")


stud = Student("Rohan",[99,98,97])
stud.getAvg()

stud2 = Student("Rahul",[99,98,97])
print(stud2.name)

#Note - If you call Student.name, it will call the name attribute from Student class.
# If the object.name i.e. stud2.name is call, the name pass "Rahul" will be called.
