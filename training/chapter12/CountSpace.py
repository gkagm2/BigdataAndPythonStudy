# 스페이스와 탭의 개수 구하기

def parseFile(file):
    print("space")
    countSpace = 0
    countTap = 0

    for line in file:

        countSpace += line.count(' ')
        countTap += line.count('\t')

    return countSpace, countTap


#fileName = input("파일의 이름을 입력하세요")
fileName = "file/spacetap.txt"
file = open(fileName, 'r', encoding="utf-8")

countSpace, countTap = parseFile(file)

print("스페이스 수 : %d, 탭의 수 = %d" % (countSpace, countTap))

file.close()
