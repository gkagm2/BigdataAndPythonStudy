# 레이블

# w = label(parent, option, ...)

# 레이블로 화면에 이미지 표시하기
from tkinter import *

window = Tk()
photo = PhotoImage(file="banana.gif")
w = Label(window, image=photo)
w.photo = photo
w.pack()

window.mainloop()