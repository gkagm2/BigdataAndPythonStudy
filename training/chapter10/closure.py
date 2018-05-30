# 클로저(closure)는 함수에 의하여 반환되는 함수이다.



# fixedNum은 어디로 저장되는거지?
def addNumber(fixedNum):
    def add(number):
        return fixedNum + number
    return add

func = addNumber(10)
print(func(20))
