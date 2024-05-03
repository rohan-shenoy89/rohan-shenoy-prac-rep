class StudentMarks():
    def __init__(self,name,marks,cls):
        self.name = name
        self.marks = marks
        self.cls = cls

    def getPercent(self):
        total_marks = sum(self.marks)
        total_sub = len(self.marks)
        result = total_marks/total_sub

        #final_result = "{:.2f}".format(result)
        return result

    def getgrade(self,result):

        if result > 90:
            return 'A+'
        elif result > 80 and result < 90:
            return 'A'
        elif result > 70 and result < 80:
            return 'B+'
        elif result > 60 and result < 70:
            return 'B'
        elif result > 50 and result < 60:
            return 'C'
        else:
            return 'D'


student = StudentMarks("Rohan",[90,91,92],"CS")
print(f"Hi {student.name} you are from {student.cls} & your overall percentage is {student.getPercent()}% and your grade is {student.getgrade(student.getPercent())}")

student2 = StudentMarks("Rahul",[40,69,99],"EC")
print(f"Hi {student2.name} you are from {student2.cls} & your overall percentage is {student2.getPercent()}% and your grade is {student2.getgrade(student2.getPercent())}")
