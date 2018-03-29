# 파일 암호화
# 평문 "come to me" 은 "FRPH WR PH"으로 바뀐다. 시저 암호 방식을 이용하여 파일을 암호화하고 복호화하는 프로그램을 작성

key = "abcdefghijklmnopqrstuvwxyz"

# 평문을 받아서 암호화하고 암호문을 반환한다.

def encrypt(n, plaintext):
    result = ""

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()


# 암호문을 받아서 복호화하고 평문을 반환한다.
def dencrypt(n, ciphertext):
    result = ""

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result

n = 3

text = "The language of truth is simple"
encrypted = encrypt(n, text)
dencrypted = dencrypt(n, encrypted)

print('평문 : ' , text)
print('암호문 : ' , encrypted)
print('복호문 : ', dencrypted)