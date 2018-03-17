# 회문(palindrone)은 앞으로 읽으나 뒤로 읽으나 동일한 문장이다.
# 예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.

def CheckPal(s):
    low = 0
    high = len(s) - 1

    while True:
        if low > high:
            return True
        a = s[low]
        b = s[high]

        if a != b:
            return False
        low += 1
        high -= 1

s = input("문자열을 입력하시오:")
s = s.replace(" ","")
print(s)

if CheckPal(s) == True:
    print("회문입니다.")
else :
    print("회문이 아닙니다.")
