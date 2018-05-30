# 정적 변수 (= 클래스 변수)
# 이들 변수는 모든 객체르르 통틀어서 하나만 생성되고 모든 객체가 이것을 공유하게 된다
# 이러한 변수를 정적 변수 또는 클래스 변수라고 한다.

class Television:
    serialNumber = 0 #이것이 정적 변수이다.
    def __init__(self):
        Television.serialNumber +=1


print(Television.serialNumber)

#객체를 3개 생성한다.
tv = Television()
print(Television.serialNumber) #생성할때마다 정적 변수가 1씩 증가하는 것을 볼 수 있다.

tv2 = Television()
print(Television.serialNumber)

tv3 = Television()
print(Television.serialNumber)