# 사용자가 직접 에러를 발생시키는 기능

def rsp(mine, yours):
    allowed = ['가위','바위','보']
    if mine not in allowed: # 가위, 바위, 보가 없다면
        raise ValueError # ValueError 를 발생시켜라
    if yours not in allowed:
        raise ValueError # ValueError 를 발생시켜라

try:
    rsp('기위','바')
except ValueError:
    print("잘못된 값을 넣었습니다!")