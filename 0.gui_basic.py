from tkinter import *

root = Tk()                           # Tk 클래스 객체
root.title("Hwangpenguin")
root.geometry("480x640+900+100")      # 소문자 x써야함 

root.resizable(True,False)            # x,y 창 크기 변경

btn1 = Button(root, text = "버튼1")
btn1.pack()                           # .pack(): 적어줘야 버튼 보임

btn2 = Button(root, fg ="red", bg="yellow", padx=15, pady=5, text = "버튼2")
btn2.pack() 

btn3 = Button(root, padx=5, pady=15, text = "버튼3")     # text길이에 따라 버튼 너비 변화/ 오,왼,위,아래 공간 설정
btn3.pack() 

btn4 = Button(root, width=5, height=15, text = "버튼4")  # text길이와 관계없이 버튼 너비 일정(고정값)
btn4.pack()

# photo = PhotoImage(file="heart.png")                     # small-projects_python\ 붙이니까 오류남
# btn5 = Button(root,image = photo)
# btn5.pack()


def btncmd():
    print("버튼 클릭!!")

btn6 = Button(root, text = "동작하는 버튼", command=btncmd)
btn6.pack()


txt= Text(root,width=20,height=5)      # enter 가능 / 여러줄 입력받을 수 있다.
txt.pack()
txt.insert(END,"글자를 입력하세요")

e= Entry(root,width=20)               # enter 불가능. 한줄로 입력받는 아이디,비번 같은 경우
e.pack()
e.insert(END,"글자 입력")              # height => 오류  / END와 0 둘다 사용가능



def btncmd():
    # 글자 출력
    print(txt.get("1.0",END))        # 1: 첫번째 라인  0: 0번째 column 위치 / END끝까지 들고오기
    print(e.get())

    # 글자 삭제
    txt.delete("1.0",END)
    e.delete(0,END)         

btn7 = Button(root, text="text,entry_Click", command = btncmd)
btn7.pack()



listbox= Listbox(root,selectmode="extended",height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(END,"포도")                      # END 소문자없이 모두 대문자로
listbox.insert(END,"귤")
listbox.pack()

def listcmd():
    # 글자 삭제
    # listbox.delete(End)                       # End: 끝부터 삭제  /  0: 맨 처음부터 삭제

    # 개수 확인
    print("리스트에는",listbox.size(),"개가 있어요")

    # 항목 확인 (시작 index, 끝 index)
    print("1번째부터 3번째까지 항목: ",listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환 ==> (0,4))
    print("선택된 항목: ",listbox.curselection())

btn_list=Button(root,text="listbox_Click",command=listcmd)
btn_list.pack()


root.mainloop()
