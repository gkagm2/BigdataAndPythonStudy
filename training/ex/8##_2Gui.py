from tkinter import *

def doingJob():
    path = inputPath.get()

    try:
        f = open(path, "r")
    except FileNotFoundError as e:
        totalMoneyLabel.configure(text=" file does not exist")
        print(str(e))
    else:
        li = []
        dicList = {}
        totalMoney = 0
        print("call showTotal")
        for line in f:
            lineWords = line.split()
            # print("word" ,lineWords)
            count = 1
            a = ""
            b = ""
            for i in lineWords:
                if count % 2 == 0:
                    a = i
                    totalMoney += int(a)
                    li.append(int(a))
                else:
                    b = i

                count += 1
            dicList[a] = b  ## add



        # print("dffff",dicList)
        li.sort()
        strList =""
        for l in li:
            strList += dicList.get(str(l))
            strList += " "

        strTotalMoney = "- 총보유금액 : " + str(totalMoney)
        strTotalList = "- 보유금액순 종목명 : " + str(strList)

        totalMoneyLabel.configure(text=strTotalMoney)
        stuffLabel.configure(text=strTotalList)
        f.close()









app = Tk()
app.geometry("500x400+5+5")
app.resizable(0, 0)
app.title("과제2")

label = Label(app, text="보유주식 파일을 입력하시오:")
label.pack()
inputPath = Entry(app)
inputPath.pack()
inputBtn = Button(app, text="입력", command=doingJob)
inputBtn.pack()
showLabel = Label(app, text="")
showLabel.pack()

totalMoneyLabel = Label(app, text="")
totalMoneyLabel.pack()
stuffLabel = Label(app, text="")
stuffLabel.pack()



app.mainloop()

