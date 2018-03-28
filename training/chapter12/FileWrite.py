import os.path

outfile = open("file/write.txt","w",encoding="UTF-8")

if os.path.isfile("write.txt") :
    print("동일한 이름의 파일이 존재 합니다.")            

else :
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010--1234-124")

outfile.close()