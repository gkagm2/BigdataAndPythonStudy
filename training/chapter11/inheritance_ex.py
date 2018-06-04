# 상속 구현하기

# 일반적인 운송수단을 나타내는 클래스이다.

class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make # 메이커
        self.model = model # 모델
        self.color = color # 자동차 색상
        self.price = price # 자동차 가격

    def setMake(self, make): #설장자 메소드
        self.make = make

    def getMake(self): # 접근자 메소드
        return self.make

    #차량에 대한 정보를 문자열로 요약하여서 반환한다.
    def getDesc(self):
            return "차량 = (" + str(self.make) + "," + \
                str(self.model) + "," + \
                str(self.color) + "," + \
                str(self.price) + ")"


class Truck(Vehicle):
    def __init__(self, make, model, color, price, payload):
        super().__init__(make, model, color, price)
        self.payload = payload

    def setPayload(self, payload): #설장자 메소드
        self.payload = payload

    def getPayload(self): # 접근자 메소드
        return self.payload



def main():
    myTruck = Truck("Tisla", "Model S", "white", 10000, 3000)
    myTruck.setMake("Tesla")
    myTruck.setPayload(2000)
    print(myTruck.getDesc())
    print(myTruck.getPayload())

main()