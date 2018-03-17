# csv 파일은 split() 메소드를 이용하여 파싱될 수 있다.
# open(), readlines(), strip() 메소드를 사용하여 csv파일에서 데이터를 읽는 프로그램을 작성해보자

fileName = input("파일이름을 입력하시오 : ")

file = open(fileName,"r")

# 파일의 각 줄에 대하여 반복한다.
for line in file.readline():

    #공백 문자를 제거한다.
    line = line.strip()

    #줄을 출력한다.
    print(line)

    #줄을 단어로 분리한다.
    words = line.split(",")

    #줄의 단어를 출력한다.
    for word in words:
        print("   ", word)

