class Student:
    def __init__(self):
        self.__id = 123
        self.__name = "John"
        # ? __variable : private field variable

    def show(self):
        print(self.__id)
        print(self.__name)


s = Student()
# * print(s.__id)
# * print(s.__name)
# ! can't access private variable from out of the class, AttributeError

s.show()

print(s._Student__id)
print(s._Student__name)
# ! obejctName._className__variable : class의 private field에 접근하는 방법
