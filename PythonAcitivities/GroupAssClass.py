class Student:
    def __init__(self, StdNumber, StdName, SubCount):
        self.StdNumber = StdNumber
        self.StdName = StdName
        self.SubCount = SubCount

    def AppendStudent(self):
        studAppend = open("StudentRec.txt","a")
        studAppend.write(f"{self.StdNumber} {self.StdName} {self.SubCount}\n")
        studAppend.close()

class Subject:
    def __init__(self, SubCode, SubDesc, NoUnits, MidGrade, FinGrade, Average, Remarks):
        self.SubCode = SubCode
        self.SubDesc = SubDesc
        self.NoUnits = NoUnits
        self.MidGrade = MidGrade
        self.FinGrade = FinGrade
        self.Average = Average
        self.Remarks = Remarks

    def AppendSubject(self):
        subAppend = open("StudentRec.txt","a")
        subAppend.write(f"{self.SubCode} {self.SubDesc} {self.NoUnits} {self.MidGrade} {self.FinGrade} {self.Average} {self.Remarks}\n")
        subAppend.close()