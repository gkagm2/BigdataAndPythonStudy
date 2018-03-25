# 버튼의 이벤트 처리

from tkinter import *

def callback():
    button2["text"] = "버튼이 클릭되었음!"

window = Tk()

button2 = Button(window, text="클릭", command=callback)
button2.pack(side=LEFT)

window.mainloop()