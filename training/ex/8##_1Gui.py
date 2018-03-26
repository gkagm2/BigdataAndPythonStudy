from tkinter import *

def isPrime(v):
    if v == 2:
        return True  #소수
    for x in range(2, v):
        if v % x == 0:
            break
        elif x == v - 1:
            return True
    return False

def getFib(value):
    list = []
    a , b = 0, 1
    while a <= value:
        list.append(a)
        a, b = b, a+b
    print()
    return list

def showList():
    list1 = []

    if isNumber(inputValue.get()):
        list1 = getFib(int(inputValue.get()))
        showLabel.configure(text=max(list1))

    else :
        showLabel.configure(text="정수를 입력해 주세요")




def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


app = Tk()
app.geometry("500x400+5+5")
app.resizable(0, 0)
app.title("과제")

label = Label(app, text="최대값을 입력하시오.")
label.pack()
inputValue= Entry(app)
inputValue.pack()
inputBtn = Button(app, text="입력", command=showList)
inputBtn.pack()
showLabel = Label(app, text="")
showLabel.pack()














app.mainloop()






