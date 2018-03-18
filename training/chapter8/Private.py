class Student:
    def __init__(self, name=None, age=0):
        self.__name = name  # double underscore로 시작하면 private변수이다.
        self.__age = age

obj = Student()


# 에러가 뜬다.
print(obj.__age)