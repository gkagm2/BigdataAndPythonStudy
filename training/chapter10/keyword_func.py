import keyword
 # for 입력시 if문 실행
name = input("변수 이름을 입력하시오")

if keyword.iskeyword(name):
    print(name, "은 예약어임")
    print("아래는 키워드 전체 리스트임")
    print(keyword.kwlist)
else :
    print(name,"은 사용할 수 있는 변수임")