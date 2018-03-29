# 임의 접근의 원리
# 위치 표시자를 이동 시킨다.

# 파일 포인터를 이동시켜서 랜덤하게 읽는다.

infile = open("file/file.txt","r+", encoding='utf-8')

str = infile.read(10) # 10개의 글자를 읽는다.
print(str)
position = infile.tell() # The method tell() returns the current position of the file read/write pointer within the file
print("현재 위치 : ",position)

position = infile.seek(0,0) # The method seek() sets the file's current position at the offset.
str = infile.read(10)
print("다시 읽은 문자열 : ",str)
infile.close()
