# 인터넷 뱅킹을 사용하다보면 계좌번호를 입력할 때, "312-02-1234567"과 같이 "-"을 사용하면 안 된다는 경고를 받는다.
# 사용자로부터 "-"가 포함된 계좌 번호를 받아서 "-"을 삭제한 문자열을 만들어보자

account = input("계좌번호를 입력하시오 ")
myAccount = ""
disword = "-"
for c in account:

    if c not in disword:
        myAccount = myAccount + c
print(myAccount)

print("")


# same code

# myAccount = ""
#
# for c in account:
#     if c != "-":
#         myAccount = myAccount + c
# print(myAccount)