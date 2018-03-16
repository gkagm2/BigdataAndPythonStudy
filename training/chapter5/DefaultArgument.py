# 함수의 인자에 값을 설정해 놓으면 적지 않아도 defualt값으로 설정된 값이 들어간다.
def greet(name,  msg = "별일없죠?"):
    print("안녕," + name +', ' + msg)

