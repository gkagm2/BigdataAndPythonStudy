# 레이블의 색상과 폰트 변경하기

from tkinter import *
from tkinter.colorchooser import *

window = Tk()

Label(window,
      text="Times Font 폰트와 빨강색을 사용합니다.",
      fg = "red",
      font = "Times 32 bold italic").pack()

Label(window,
      text="Helvetica 폰트와 녹색을 사용합니다.",
      fg = "green",
      bg = "yellow",
      font = "Helvetica 20 bold italic").pack()

window.mainloop()