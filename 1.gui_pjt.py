from tkinter import *
'''
프레임 사이 간격이 너무 좁을때 
==> frame.pack(padx= 5, pady= 5) 넣어보자
==> 버튼에서 Button(master, padx= 5, pady= 5 ): 버튼 내 text와 간격
==> 버튼에서 Button.pack(padx= 5, pady= 5 ): 버튼과 프레임 사이 간격
'''

root = Tk()                   # Tk 클래스 객체
root.title("사진 합치기")                    

# 파일 프레임 (파일추가, 파일삭제 버튼 만들기)
frame_file = Frame(root)
frame_file.pack(fill="x", padx= 5, pady= 5)     # x로 펼치기

btn_addfile = Button(frame_file, padx= 5, pady= 5, width = 12, text= "파일추가")  
btn_addfile.pack(side="left")

btn_addfile = Button(frame_file, padx= 5, pady= 5, width = 12,text= "파일추가") 
btn_addfile.pack(side="right")

# 리스트 프레임
frame_list = Frame(root)
frame_list.pack(fill= "both", padx= 5, pady= 5)         # frame도 .pack(fill= "both")로 꽉 채울수 있군

scroll = Scrollbar(frame_list)
scroll.pack(side= "right", fill= "y")

list_file = Listbox(frame_list, selectmode = "extended", height =15, yscrollcommand = scroll.set)
list_file.pack(side = "left", fill= "both", expand = True)

scroll.config(command= list_file.yview)

# 저장경로 프레임 만들기
frame_path = LabelFrame(root, text="저장경로")
frame_path.pack(fill="x", padx= 5, pady= 5, ipady=5)

txt_path = Entry(frame_path)                              # enter 불가능. 한줄로 입력받는 아이디,비번 같은 경우
txt_path.pack(side= "left",fill= "x", expand= True, ipady= 4, padx= 5, pady= 5)     # fill= "x", expand=True 안써도 똑같은데 왜 쓰지? 
                                                                  # ipady = 4 : 높이 변경
btn_search = Button(frame_path, width=10, text="찾아보기")
btn_search.pack(side= "right", padx= 5, pady= 5)


# 옵션 프레임 만들기
import tkinter.ttk as ttk
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx= 5, pady= 5, ipady=5)

# 너비 레이블
lbl_width = Label(frame_option,text="가로넓이",width=8)
lbl_width.pack(side= "left", padx= 5, pady= 5)

# 너비 콤보박스
v_width= ["원본유지", "1024", "800", "600"]
combo_width= ttk.Combobox(frame_option, values= v_width, state="readonly", width=8)
combo_width.current(0)
combo_width.pack(side= "left", padx= 5, pady= 5)

# 간격 레이블
lbl_gap = Label(frame_option,text="간격",width=8)
lbl_gap.pack(side= "left", padx= 5, pady= 5)

# 간격 콤보박스
v_gap= ["넓음","보통","좁음","없음"]
combo_gap= ttk.Combobox(frame_option, values= v_gap, state="readonly", width=8)
combo_gap.current(1)
combo_gap.pack(side= "left", padx= 5, pady= 5)

# 포맷 레이블
frame_lbl = Label(frame_option,text="포맷",width=8)
frame_lbl.pack(side= "left", padx= 5, pady= 5)

# 포맷 콤보박스
v_format= ["PNG","JPG","GMP"]
combo_format= ttk.Combobox(frame_option, values= v_format, state="readonly", width=8)
combo_format.current(0)
combo_format.pack(side= "left", padx= 5, pady= 5)


# 진행상황 progress bar

frame_progress = LabelFrame(root, text= "진행상황")
frame_progress.pack(fill="x", padx= 5, pady= 5)

p_var = DoubleVar()
progress_var = ttk.Progressbar(frame_progress, maximum = 100, variable= p_var)
progress_var.pack(fill="x", padx= 5, pady= 5)


# 실행 프레임 만들기
frame_run = Frame(root)
frame_run.pack(fill="x", padx= 5, pady= 5)

btn_close = Button(frame_run, padx= 5, pady= 5, width = 12,text="닫기", command= root.quit)
btn_close.pack(side="right", padx= 5, pady= 5)

btn_run = Button(frame_run, padx= 5, pady= 5, width = 12, text="시작")
btn_run.pack(side= "right", padx= 5, pady= 5)


root.resizable(False,False)  
root.mainloop()
