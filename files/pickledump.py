import pickle
import student

f = open("student.dat", "wb")
s = student.Student(123, "John", 90)
pickle.dump(s, f)
# ? pickle.dump(obj, file)
f.close()