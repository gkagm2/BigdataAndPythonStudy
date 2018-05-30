# 생성자의 예

class Counter: # 클래스를 생성
    def __init__(self, something): # 생성자임 (객체가 생성될 때 객체를 기본값으로 초기화하는 특수한 메소드이다.
        self.count = 0 # 클래스 내 count 변수 생성 후 초기화
    def reset(self):
        self.count = 0 # 클래스 내 count 변수를 0으로 reset한다.
    def increment(self):
        self.count += 1 # 클래스 내 count 변수를 1씩 증가시킨다.
    def get(self):
        return self.count # 카운터 변수를 리턴한다.



# 메소드 정의

class Television:

    def __new__(cls, *args, **kwargs):
        print("television start")

    def __init__(self,channel=0, volume=0, on=True ): # 생성자
        self.channel = channel # 각각의 인자를 클래스 내 변수에 저장
        self.volume = volume
        self.on = on
    def show(self): # show 메소드는 print로 출력
        print(self.channel, self.volume, self.on)

    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self):
        return self.channel

    def setVolume(self,volume):
        self.volume = volume
    def getVolume(self):
        return self.volume

    def somethnig(self):
        pass # pass는 실행할 코드가 없다는 의미이다. continue는 다음 순번의 loop를 돌도록 강제하는것을 의미,
        print("pass 이후에도 이 문장은 실행됨")

t = Television()
t.show()

t2 = Television(9, 19, True)

t2.show()
t2. setChannel(11)
t2.show()

# Private : double underscore(__)로 시작하는 변수

class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age


obj = Student()
# print(obj.__age) # 이렇게 하면 오류



