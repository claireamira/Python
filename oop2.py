class Student:
    def __init__(self, name, maths, sci, eng):
        self.name = name
        self.maths = maths
        self.sci = sci
        self.eng = eng
    
    def getAverage(self):
        avg = (self.maths+self.sci + self.eng) / 3
        return round(avg)
    
    def compare(self, anotherStd):
        if self.getAverage() > anotherStd.getAverage():
            return [self.name, anotherStd.name]
        return [anotherStd.name, self.name]
    
    @staticmethod
    def rank(students):
        students.sort(key=lambda x: x.getAverage(), reverse = True)
        f = open("results.txt", "w")
        f.write("RESULTS\n\n")
        f.write("Rank Name Maths Sci Eng Avg\n\n")
        count = 1
        for student in students:
            f.write(f"{count} {student.name} {student.maths} {student.sci} {student.eng} {student.getAverage()}\n")
            count = count + 1
        f.close
    
    def __str__(self):
        return f"Name: {self.name}, Average: {self.getAverage()}" 


studentList = []

while True:
    name = input("Enter student Name. Enter q to exit:")
    if name == "q":
        break
    maths = int(input("Enter maths: "))
    sci = int(input("Enter Science: "))
    eng = int(input("Enter English: "))

    std = Student(name, maths, sci, eng)
    studentList.append(std)

Student.rank(studentList)