# 매출 파일 처리

#입력 파일 이름과 출력 파일 이름을 받는다.
infilename = input("입력 파일 이름")
outfilename = input("출력 파일 이름")


#입력과 출력을 위한 파일을 연다.
try :
    infile = open("file/" + infilename,"r", encoding="UTF-8")
    outfile = open("file/" + outfilename, "w", encoding="UTF-8")
except IOError:
    print("파일을열 수 없습니다.")

else :
    # 합계와 횟수를 위한 변수를 정의한다.

    sum = 0
    count = 0
    for line in infile:
        dailySale = int(line)
        print(dailySale)
        sum = sum + dailySale
        count = count + 1

    # 총매출과 일평균 매출을 출력 파일에 기록한다.
    outfile.write("총매출 = " + str(sum) + '\n')
    outfile.write("평균 일매출 = " + str(sum / count))

    infile.close()
    outfile.close()



