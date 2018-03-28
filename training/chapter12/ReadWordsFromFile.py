# 파일에서 단어 읽기
infile = open("file/file.txt","r", encoding="utf-8" )
for line in infile:
    line = line.rstrip()
    word_list = line.split() # 단어마다 짤막짤막하게 짤라서 리스트형태로 변환
    print(word_list)
    for word in word_list:
        print(word)

infile.close()