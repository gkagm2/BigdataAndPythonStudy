# key 매개변수

# 정렬을 하다보면 정렬에 사용되는 키를 개발자가 변경해주어야 하는 경우가 종종 있다.

print(sorted("The headlth know not of their health, but only the sick".split(), key=str.lower))



students = [ ('홍길동', 3.9, 20160303),('김철수',3.0, 20160302),(
    '최자영',4.3,20160301)]


print(sorted(students, key= lambda student: student[2]))


class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number

    def __repr__(self): # what is it? # print문에 객체 이름만 입력해도 무엇을 출력할지에 대해 설정할 수 있음
        return repr((self.name, self.grade, self.number))


students = [
    Student('홍길동', 3.9, 20160303),
    Student('김철수', 3.0, 20160302),
    Student('최자영', 4.3, 20160301),
]

# 오름차순 정렬과 내림차순 정렬
print(sorted(students, key = lambda student: student.number, reverse=True))



############################ 키를 이용한 정렬 ###########################

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "<이름: %s, 나이: %s>" % (self.name, self.age)
    
def keyAge(person):
    return person.age

people = [Person("홍길동", 20), Person("김철수",35), Person("최자영", 38)]

print(sorted(people, key=keyAge, reverse=True)) # 이 부분을 보면 정확히 key가 무엇인지 이해함



