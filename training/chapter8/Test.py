#객체를 함수로 전달할 때
# 작성한 객체가 전달되면 함수가 객체를 변경할 수 있다.

# 사각형을 클래스로 정의한다
class Rectangle:
    def __init__(self, side = 0):
        self.side = side

    def getArea(self):
        return self.side**2

# 사각형 객체와 반복횟수를 받아서 변을 증가시키면서 면적을 출력한다.
def printAreas(r, n):
    while n >= 1:
        print(r.side, "\t", r.getArea())
        r.side = r.side + 1
        n = n - 1

# printAreas()을 호출하여 객체의 내용이 변경되는지를 확인한다.
myRect = Rectangle()
count = 5
printAreas(myRect, count)
print("사각형의 변=", myRect.side)
print("반복횟수=", count)