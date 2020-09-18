from tkinter import *

root = Tk()                           # Tk 클래스 객체
root.title("Alarm")
root.geometry("480x640+900+100")      # 소문자 x써야함 

root.resizable(True,True)            # x,y 창 크기 변경

label1 = Label(root, text="좋은 아침이에요:)")
label1.pack()

wall = PhotoImage(file = "best.png")
wall_label = Label(root, image=wall)
wall_label.place(x=-2,y=120)         # x=0, y=0으로 하고 이미지 봐서 조정함


def change():
    label1.config(text="좋은 시작이에요♥")

btn1 = Button(root, text = "클릭", command=change)
btn1.pack()

root.mainloop()
