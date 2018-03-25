# Button 색상

from tkinter import *
window = Tk()

button = Button(window, text="버튼을 클릭하세요")

button.pack() # pack을 먼저 하고

# 그 후에 바꿔도 적용되는 듯.
button["fg"] = "yellow" # fg 뜻이 font ground?
button["bg"] = "green" #bg 뜻이 back ground


window.mainloop()
