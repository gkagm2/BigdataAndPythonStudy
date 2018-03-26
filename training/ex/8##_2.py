dicList = {}




filePath = input("보유주식 파일을 입력하시오:")
f = open(filePath, "r")
totalMoney = 0
li = []
for line in f:
    lineWords = line.split()
    #print("word" ,lineWords)
    count = 1
    a= ""
    b= ""
    for i in lineWords:
        if count % 2 == 0:
            a = i
            totalMoney += int(a)
            li.append(int(a))
        else:
            b = i


        count += 1
    dicList[a] = b ## add


#print("dffff",dicList)
li.sort()
print("- 총보유금액 : ",totalMoney)
print("- 보유금액순 종목명 : ", end= " ")
for l in li:
    print(dicList.get(str(l)), end=" ")
