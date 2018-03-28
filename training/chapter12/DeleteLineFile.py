# 줄바꿈 기호 삭제하기

infile = open("file/file.txt","r", encoding="utf-8")
for line in infile:
    line = line.rstrip()
    print(line);
infile.close()