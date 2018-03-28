# file example1

infile = open("file/file.txt","r", encoding='UTF-8')
s = infile.read(10) # 10글자를 읽어온다.
print(s)
infile.close()