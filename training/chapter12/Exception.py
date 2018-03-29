# exception

# 구조
# try :
#     예외가 발생할 수 있는 문장
# except 오류내용:
#     예외를 처리하는 문장

# 다중 예외 처리 구조
# try:
#     예외가 발생할 수 있는 문장
# except Exception1:
#     Exception1이면 이 블록이 실행된다
# except Exception2:
#     Exception2이면 이 블록이 실행된다
# else:
#     예외가 없는 경우에 실행된다.

x, y = 2, 0
try:
    z = x / y
except ZeroDivisionError:
    print("0으로 나누는 예외")

