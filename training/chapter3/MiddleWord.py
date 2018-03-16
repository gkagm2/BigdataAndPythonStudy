#중간 문자 얻기
str = input("문자열을 입력하시오:")

length = len(str) #str의 길이를 구한다.

if length % 2 == 1: #홀수면
    ch1 = str[length//2]
    print("중앙글자는 ", ch1)
else:
    ch1 = str[length//2 - 1]
    ch2 = str[length//2]
    print("중앙글자는 " ,  ch1, ch2)

