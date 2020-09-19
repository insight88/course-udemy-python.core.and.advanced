class Student:
    major = "CSE"
    # ? static field : 모든 class에 적용되는 common instance

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name


s1 = Student(1, "John")
s2 = Student(2, "Bill")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
