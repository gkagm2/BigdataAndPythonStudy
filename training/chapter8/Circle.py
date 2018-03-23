# 원을 클래스도 표시해보자. 원은 반지름(radius)을 가지고 있다.
# 원의 넓이와 둘레를 계산하는 메소드도 정의해보자. 설정자와 접근자 메소드도 작성한다.

import math

class Circle:
    def __init__(self, radius=1.0): #default value
        self.__radius = radius

    def setRadius(self,r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area

    def calcCircum(self):
        circumference = 2.0 * math.pi * self.__radius
        return circumference


c1 = Circle(10)
print("원의 반지름 =" , c1.getRadius())
print("원의 넓이 = ", c1.calcArea())
print("윈의 둘레 = ", c1.calcCircum())