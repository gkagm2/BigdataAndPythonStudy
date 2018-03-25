# 레이블에 이미지와 텍스트를 동시에 나타내기

from tkinter import *

window = Tk()
photo = PhotoImage(file="banana.gif")
w = Label(window, image=photo).pack(side="left")
message = """바나나는 맛있어~~ 바나나! 오 예! 바나나!!
아하핳하! 바나나는 최고야~~ 베이베~
바나나!!!!!!!
"""

w2 = Label(window, justify=LEFT, padx=10, text=message).pack(side="right")
window.mainloop(

)
