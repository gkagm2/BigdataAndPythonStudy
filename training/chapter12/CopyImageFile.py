# Image file copy


filename1 = input("원본 파일 이름을 입력하시오:")  # path : file/image.png
filename2 = input("복사 파일 이름을 입력하시오:")
try:
    infile = open(filename1, "rb") # read binary file
except FileNotFoundError:
    print("File can't found")
    exit()
else:
    outfile = open(filename2, "wb") # write binary file

    # 입력 파일에서 1024 바이트씩 읽어서 출력 파일에 쓴다
    while True:
        copy_buffer = infile.read(1024) # 1024 byte
        if not copy_buffer:
            break
        outfile.write(copy_buffer)

    infile.close()
    outfile.close()



print("copy complete " + filename1 + " to " + filename2)
