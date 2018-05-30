# static으로 할 때는

class StaticClassEx:
    def show(name): # self 를 뺀다.
        print("hello ", name)


print(StaticClassEx.show("jang")) # 그럼 바로 사용할 수 있다.




class StaticClassEx2:
    def show(self, name):#self가 있으면
        print("hello ")

#print(StaticClassEx2.show("jang")) # 바로 사용할 수 없다. 인스턴스를 만들어줘야 한다.

# ins = StaticClassEx2
# ins.show("e")
# ins.show("jang")


