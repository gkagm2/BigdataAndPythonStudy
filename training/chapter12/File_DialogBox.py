from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename() # file dialog box open!
if readFile != None:
    infile = open(readFile, "r", encoding="utf-8")

for line in infile.readline(): #한 줄을 가져옴.
    line = line.strip() # 그 줄에서 stript() 메소드를 사용하여 한 단어씩 나눔.
    print(line)

infile.close()

