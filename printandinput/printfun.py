print()
print("Hello"*3)
print("All the power \n is with in you")

a, b = 10, 20
print(a, b, sep='++++')

name = "john"
marks = 94.5678

print("Name is", name, "Marks are", marks)
print("Name is %s,Marks are %.3f" % (name, marks))
# ? %s : placeholder for string data, %f : placeholder for float data, .3 : display 3 decimal numbers

print("Name is {},Marks are {}".format(name, marks))

print("Name is {0},Marks are {1}".format(name, marks))
