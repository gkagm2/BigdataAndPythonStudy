# 메소드 정의

# 메소드는 클래스 안에 정의된 함수이므로 함수를 정의하는 것과 아주 유사함
# 첫 번째 매개변수는 항상 self이어야 함

class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel;
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel = channel;
    def getChannel(self):
        return self.channel

t = Television(9,10,True)

t.show()
t.setChannel(11)
t.show()