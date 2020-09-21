from tkinter import *

root = Tk()                           # Tk 클래스 객체
root.title("Hwangpenguin")
root.geometry("480x640+900+100")      # 소문자 x써야함 

root.resizable(True,True)            # x,y 창 크기 변경
'''
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
'''


# 버튼에 command넣기
'''
def btncmd():
    print("버튼 클릭!!")

btn6 = Button(root, text = "동작하는 버튼", command=btncmd)
btn6.pack()
'''

txt= Text(root,width=20,height=1)      # enter 가능 / 여러줄 입력받을 수 있다.
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



# 체크박스: 값 2개 중 택일 / 각 체크박스마다 variable에 각각 다른 값 넣어줘야 함

chk_var1 = IntVar()                        # chk_var에 Int형으로 값을 저장
chkbox = Checkbutton(root,text="체크하세요",variable=chk_var1)     # 체크박스: 변수에 값을 저장해서 씀
chkbox.select()
chkbox.pack()

chk_var2 = IntVar()                              
chkbox2 = Checkbutton(root,text="체크!",variable=chk_var2)
chkbox2.pack()


def chkcmd():
    print(chk_var1.get())                # 0: 체크해제  1: 체크
    print(chk_var2.get())      

btn1 = Button(root,text="체크박스",command=chkcmd)
btn1.pack() 



# 라디오버튼: 여러개 값 중 택일 / 각 버튼마다 variable에 각각 다른 값 넣지 않고 같은 값 넣어서 통째로 함!

Label(root,text="메뉴를 선택하세요").pack()

burger_var= IntVar()                    # Int 형으로 저장
btn_burger1= Radiobutton(root,text="햄버거",value=1,variable=burger_var)
btn_burger1.select()
# btn_burger2= Radiobutton(root,text="치즈버거",value=2,variable=burger_var)
btn_burger3= Radiobutton(root,text="치킨버거",value=3,variable=burger_var)

btn_burger1.pack()
# btn_burger2.pack()
btn_burger3.pack()


Label(root,text="주스를 선택하세요").pack()

juice_var= StringVar()
btn_juice1= Radiobutton(root,text="콜라",value="콜라",variable=juice_var) 
btn_juice1.select()
# btn_juice2= Radiobutton(root,text="사이다",value="사이다",variable=juice_var)
btn_juice3= Radiobutton(root,text="오렌지주스",value="오렌지주스",variable=juice_var)

btn_juice1.pack()
# btn_juice2.pack()
btn_juice3.pack()

def radiocmd():
    print(burger_var.get())             # 선택한 값의 value 반환(1,2,3)
    print(juice_var.get())
intbtn= Button(root,text="라디오버튼1",command=radiocmd)
intbtn.pack()



import tkinter.ttk as ttk

dates = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root,height=5, values= dates)
combobox.set("날짜를 선택하세요")
combobox.pack()

readonly_combo = ttk.Combobox(root, height=10, values= dates, state="readonly")
readonly_combo.current(0)
readonly_combo.pack()


def combocmd():
    print(combobox.get())
    print(readonly_combo.get())

combobtn = Button(root,text="선택",command=combocmd)
combobtn.pack()





# 12. 메뉴 

def file_create():
    print("새 파일을 만듭니다.")

menubar = Menu(root)                           # 상위 메뉴 생성

menu_1 = Menu(menubar,tearoff=0)               # 하위 메뉴 생성 / tearoff=0  ===> 하위 메뉴 떠다니지 않게 해줌
menu_1.add_command(label="New file",command=file_create)
menu_1.add_command(label="New window")
menu_1.add_separator()
menu_1.add_command(label= "Open file...")  
menu_1.add_separator()
menu_1.add_cascade(label="Save all", state="disable")   #비활성화 ==> 클릭 불가능
menu_1.add_separator()
menu_1.add_command(label="Exit",command= root.quit)     # root.quit  ==> 모든창 끄든

menubar.add_cascade(label= "File",menu = menu_1)        
''' 상위 메뉴 탭 레이블 설정  /  하위메뉴인 menu_1을 상위메뉴인 menubar에 연결    
    하위메뉴인 menu_1이 정의된 상태에서면 작동하므로 앞에 적으면 안된다 '''


# Edit 메뉴(빈 값)
menubar.add_cascade(label= "Edit")                      # 세부 메뉴가 없다


# Lang 메뉴(라디오 버튼)
menu_2 = Menu(menubar,tearoff=0)
menu_2.add_radiobutton(label="Sunday")
menu_2.add_radiobutton(label="Monday")
menu_2.add_radiobutton(label="Tuesday")

menubar.add_cascade(label= "Day", menu= menu_2)


# View 메뉴(체크박스)
menu_3 = Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label= "Show Minimap")

menubar.add_cascade(label="View", menu= menu_3)

root.config(menu=menubar)




# 13. 메세지 박스
import tkinter.messagebox as msgbox
'''
import 해주어야 한다! 
'''

def info():
    msgbox.showinfo("알림", "정상적으로 예매되었습니다.")       #msgbox.showinfo(타이틀, 메세지박스 안 내용)

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")      

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")      

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")      

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류가 발생했습니다. 다시 예매하시겠습니까?")      


# 사용자로부터 값을 받아서 응답에 맞는 처리해주기
def yesnocancel():
    response = msgbox.askyesnocancel(title= None, message = "예매내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하겠습니까?")
    print("응답: ", response)                     # True, False,None
    if response == 1:      # 예
        print("예")
    elif response == 0:    # 아니오
        print("아니오")
    else:                  # 취소
        print("취소")

Button(root,text="알림",command=info).pack()
Button(root,text="경고",command=warn).pack()
Button(root,text="에러",command=error).pack()
Button(root,text="확인 / 취소",command=okcancel).pack()
Button(root,text="재시도 / 취소",command=retrycancel).pack()
Button(root,text="예 / 아니오 / 취소",command=yesnocancel).pack()




# 14. 프레임
''' 여러 위젯들을 하나의 프레임에 넣어서 관리할 수 있다 .
    pack() 으로 위젯의 위치 설정이 가능하다.     '''

Label(root, text="메뉴를 선택해주세요").pack(side= "top")    # side = "top" ==> 레이블 위치 설정
Button(root,text= "주문하기").pack(side = "bottom")         # 버튼 아래에 위치시키기

icecream_frame = Frame(root,relief="solid",  bd=1)
icecream_frame.pack(side= "left", fill = "both", expand = True)

Button(icecream_frame, text= "딸기").pack()
Button(icecream_frame, text= "바닐라").pack()
Button(icecream_frame, text= "망고").pack()
# check_bar = StringVar()                              
# Checkbutton(root,text="바닐라",variable= check_bar).pack()
# Checkbutton(root,text="딸기",variable= check_bar).pack()
# Checkbutton(root,text="망고",variable= check_bar).pack()


root.mainloop()
