# 클래스로 포레임 감싸기

from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window, text="hello", command=self.hello, fg="red")
        helloB.pack(side=LEFT,padx=10)
        quitB = Button(window, text="Quit", command=self.quit)
        quitB.pack(side=LEFT,padx=10)
        window.mainloop()

    def hello(self):
        print("Hello 버튼이 클릭되었음!")
    def quit(self):
        print("Quit 버튼이 클릭되었음!")



App()