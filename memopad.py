import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("680x480")
# root.resizable(True,True)       지워도 크기조절 자유롭게 가능

# frame = Frame(root)
# frame.pack()
'''
txt말고 다른 위젯이 없으므로 스크롤바를 바로 root에 넣기!
'''
scroll= Scrollbar(root)
scroll.pack(side="right",fill="y")

# txt= Text(frame,width=680,height=480,yscrollcommand=scroll.set)
txt = Text(root, yscrollcommand = scroll.set)       # 전체화면에 꽉차게 만들기
txt.pack(fill="both", expand=True) 
''' 
fill: 요구되었지만 사용되지 않은 공간에 대해 위젯이 늘어남
expand: 요구되지 않은 공간을 사용하고 싶을때 사용. 현재틀에서 요구할 수 있는 모든 공간 요구
set: 위젯에 스크롤바 적용(스크롤바 연결)
'''
scroll.config(command = txt.yview)


filename= "mynote.txt"

def openfile():     # filename 이라는 파일이 있는지 없는지 확인하고 열어줘야함!! (내가 빼뜨린 부분)
    if os.path.isfile(filename):
        with open(filename, "r", encoding = "utf8") as file:
            txt.delete("1.0",END)      # 메모장 본문에 있던 내용을 지워주고 file에 있는 내용 읽어야함!
            txt.insert(END, file.read())     # 파일내용을 본문에 입력
'''
os.path.isfile(filename))  ==> filename이라는 파일 있으면 True, 없으면 False
with open() as ㅇㅇ:  ==> with open뒤에 : 를 붙여줌
txt.insert(END, file.read())  ==> END: 끝에 붙여줌  /  file.read(): 파일 통째로 읽기
txt.delete(index, index)  ==> 앞 내용 지워주기 index는 범위!
'''

def savefile():
    with open(filename, "w", encoding = "utf8") as file:
        file.write(txt.get("1.0",END))


# def openfile():
#     file_note = open("mynote.txt", "w", encoding = "utf8")   # file_score : 파일 객체를 저장하는 변수의 이름
#     print(txt.get("1.0",END), file = file_note)
#     file_note.close()

# def savefile():
#     file_note = open("mynote.txt", "r", encoding = "utf8")
#     line = file_note.readline()
#     txt.insert(END,line)
     
#     file_note.close() 


menubar= Menu(root)

menu1= Menu(menubar,tearoff = 0)
menu1.add_command(label="열기",command=openfile)
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