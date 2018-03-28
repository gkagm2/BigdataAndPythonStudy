# 텍스트 입출력 기법
# 데이터 추가하기

outfile = open("file/file.txt","a", encoding="utf-8") # 'a' mean is append

outfile.write("\n" + "최무선 010-1111-2222")
outfile.write("\n" + "정무중 010-2222-3333")

outfile.close()