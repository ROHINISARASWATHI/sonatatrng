class student:
    def __init__(self , student_id, student_name):
        self.stid = student_id
        self.stname = student_name

    def getstudent(self):
        return self. stid , self.stname

std1=student(22986,'rohini')
x=std1.getstudent()
print(x)
setattr(std1, 'student_class',10)
print(getattr(std1,'student_class'))
delattr(std1,'stname')
print(hasattr(std1, 'student_name'))
st1=student(22986,'rohini')
x=st1.getstudent()
print(x)