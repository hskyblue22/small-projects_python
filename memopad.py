from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("680x480")
root.resizable(True,True)

frame = Frame(root)
frame.pack()
scroll= Scrollbar(frame)
scroll.pack(side="right",fill="y")

txt= Text(frame,width=680,height=480,yscrollcommand=scroll.set)
txt.pack() 

scroll.config(command = txt.yview)


def savefile():
    file_note = open("mynote.txt", "w", encoding = "utf8")   # file_score : 파일 객체를 저장하는 변수의 이름
    print(txt.get(), file = file_note)
    file_note.close()


menubar= Menu(root)

menu1= Menu(menubar,tearoff = 0)
menu1.add_command(label="열기")
menu1.add_command(label="저장",command= savefile)
menu1.add_separator()
menu1.add_command(label="끝내기",command=root.quit)

menubar.add_cascade(label= "파일",menu= menu1) 
menubar.add_cascade(label= "편집") 
menubar.add_cascade(label= "서식") 
menubar.add_cascade(label= "보기") 
menubar.add_cascade(label= "도움말") 

root.config(menu=menubar)            # 적어줘야지 메뉴 나타남!!


root.mainloop()