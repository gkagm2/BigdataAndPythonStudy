# tkinter(Tk Interface)는 파이썬에서 그래픽 사용자 인터페이스(GUI)를 개발할 때 필요한 모듈
# tkinter는 예전부터 유닉스 계열에서 사용되던 Tcl/Tk 위에 객체 지향 계층을 입힌 것.
# Tk는 John Ousterhout에 의하여 Tcl 스크립팅 언어를 위한 GUI확장으로 개발


from tkinter import *

window = Tk() # root window 생성

label = Label(window, text="Hello world") #label widget 생성
label.pack()

window.mainloop() # event handler 시작

#tkinter 프로그램은 이벤트에 기반을 두고 동작 됨.

# 메인 프로그램 -> 호출한다 -> 라이브러리 함수(소프트웨어 라이브러리) -> 호출한다 -> 콜백함수
# 이벤트가 발생하면 라이브러리에서 사용자가 지정한 콜백 함수를 호출하는 개념임