from tkinter import *

root = Tk()                         
root.geometry("350x430")      


# 15. 스크롤바 : 스크롤바와 대상이 되는 위젯을 하나의 프레임에 넣는게 관리하기 좋다.
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill ="y")        # 스크롤바 세로로 꽉 차도록 해줌

# set 없으면 내려가지 않음
listbox = Listbox(frame,selectmode="extended", height =10,yscrollcommand=scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command = listbox.yview)

'''
listbox => yscrollcommand = scrollar.set
scrollbar.config(command= listbox.yview)
서로 매핑시켜줘야함
'''



root.mainloop()
