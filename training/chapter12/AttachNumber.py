# 텍스트 파일을 열어서 각 줄의 앞에 번호를 매겨서 다시 파일에 쓰는 프로그램 작성

infile = open("file/file.txt","r",encoding="utf-8")
outfile = open("file/output.txt","w",encoding="utf-8")

number = 1
for file in infile:

    outfile.write(str(number) + ": " + file)
    number += 1

infile.close()
outfile.close()
