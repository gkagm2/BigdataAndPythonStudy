# 폰트

# 폰트를 튜플로 지정할 수 있는데 여기에는 (폰트이름, 폰트의 크기, 폰트 스타일)과 같은 형식을 사용함
#  ("Times",10,"bold")
#  ("Helvetica",10,"bold italic")
#  ("Symbol",8)

# 문자열로도 지정
#  w = Label(master, text="Helvetica", font="Helvetica 16")


# 폰트 사이즈 조절
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root = tk.Tk()

        self.customFont = font.Font(family="Helvetica", size=12)

        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello, world", font=self.customFont)
        buttonframe.pack()
        label.pack()

        bigger = tk.Button(root, text="폰트를 크게", command=self.BigFont)
        smaller = tk.Button(root, text="폰트를 작게", command=self.SmallFont)
        bigger.pack()
        smaller.pack()

        root.mainloop()

    def BigFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size+2)

    def SmallFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size-2)

app = App()