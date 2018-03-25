# 버튼의 텍스트 변경

from tkinter import *

window = Tk()

b1 = Button(window, text="첫번째 버튼")
b2 = Button(window, text="두번째 버튼")
b1.pack(side=LEFT, padx=10)
b2.pack(side=RIGHT, padx=10)

# 이렇게 변경가능
b1["text"] = "ONE"
b2["text"] = "TWO"

window.mainloop()