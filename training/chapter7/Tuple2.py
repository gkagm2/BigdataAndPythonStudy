student1 = ("철수",19,"CS")

(name, age, major) = student1
print(name)
# name = fuck # tuple로 되어서 변경 불가능
print(age)
print(major)

name,age,major = student1
name = "fuck" # 변경 가능
print(name)
print(age)
print(major)
