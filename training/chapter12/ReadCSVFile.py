# CSV (Comma Separated Values) 형식은 엑셀과 같은 스프레드 쉬트나 데이터베이스에서 가장 널리 사용되는 입출력 형식.
# 파이썬은 CSV 형식을 읽기 위해서 csv라고 하는 모듈을 제공함
# 이 모듈을 이용하면 CSV파일을 쉽게 읽을 수 있다.

# open file

f = open("file/file2.txt", "r", encoding='utf-8')

# process each line in the file
for line in f.readlines():

    # remove whitespace characters
    line = line.strip()


    print("print :" + line)

    # split ,
    parts = line.split(',')
    print("parts " , parts)

    # field print in each parts
    for part in parts:
        print("  ", part)




f.close()

