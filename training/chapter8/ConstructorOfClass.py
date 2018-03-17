# 생성자(constructor)는 객체가 생성될 때 객체를 기본값으로
# 초기화하는 특수한 메소드이다.

class Counter:
    def __init__(self): # 생성자임.
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count


