# 특수 메소드
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # special method in class
    def __add__(self, other):
        return Vector2D(self.x + other.x , self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x , self.y - other.y)

    def __eq__(self, other):
        return Vector2D(self.x == other.x and self.y == other.y)

    # if you print this class than will use this method __str__
    def __str__(self):
        return '(%g %g)' % (self.x, self.y)


u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
# this fuction have same working operation +,-, *, etc... like c++. c++ have operator
a = u + v # used __add__
z = u - v # used __sub__
print(a)
print(z)