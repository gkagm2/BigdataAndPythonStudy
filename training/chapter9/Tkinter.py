# tkinter(Tk Interface)는 파이썬에서 그래픽 사용자 인터페이스(GUI)를 개발할 때 필요한 모듈
# tkinter는 예전부터 유닉스 계열에서 사용되던 Tcl/Tk 위에 객체 지향 계층을 입힌 것.
# Tk는 John Ousterhout에 의하여 Tcl 스크립팅 언어를 위한 GUI확장으로 개발


from tkinter import *

window = Tk() # root window 생성

label = Label(window, text="Hello world") #label widget 생성
label.pack()

window.mainloop() # event handler 시작