import os
from tkinter import *                    # __all__
from tkinter import filedialog           # sub module이라서 따로 정의해줌
import tkinter.ttk as ttk                # 콤보박스
import tkinter.messagebox as msgbox      # 메세지박스
from PIL import Image                    # 이미지 라이브러리 사용 (Python Imaging Library)

'''
프레임 사이 간격이 너무 좁을때 
==> frame.pack(padx= 5, pady= 5) 넣어보자
==> 버튼에서 Button(master, padx= 5, pady= 5 ): 버튼 내 text와 간격
==> 버튼에서 Button.pack(padx= 5, pady= 5 ): 버튼과 프레임 사이 간격
'''

root = Tk()                   # Tk 클래스 객체
root.title("사진 합치기")                    


# 파일 추가_____  initialdir = "C:/": 최초에 C:/ 경로를 보여줌
        
def add_file():
    files = filedialog.askopenfilenames(title= "이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일","*.png"), ("모든 파일","*.*")), initialdir = r"C:\Users\황서연\Desktop")   
    # initialdir= "C:/"  => C드라이브에서 시작 

    for file in files:
        list_file.insert(END, file)


def del_file():
    # print(list_file.curselection())     ==> 선택한 파일의 순서나옴    예:(0,2)
    for index in reversed(list_file.curselection()):       # reversed: 0부터 삭제하면 파일 순서가 바뀌어서 원치 않는 것 삭제하게 됨
        list_file.delete(index)  

'''
list1= [1,2,3,4,5]
print(list1)               => [1,2,3,4,5]
list1.reverse                                  list.reverse : list의 배열 바꿈
print(list1)               => [5,4,3,2,1]

list2= reversed(list1)                         reversed(list) : list의 배열 바꾸지 않음/ 실제값에 영향 X
print(list1)               => [5,4,3,2,1] 
print(list(list2))         => [1,2,3,4,5]
'''

# 저장 경로 (폴더_밑에 지정한 파일명으로 저장)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected =="" :              # 사용자가 취소를 누를때
        return
    txt_path.delete(0, END)                # 원래 값 삭제부터 해줌.   Entry.delete(0, END)  /  Text.delete("1.0", END) 
    txt_path.insert(0, folder_selected)


# 이미지 통합
def merge_image():

    # 옵션 조정!

    # 가로너비
    img_width = combo_width.get()
    if img_width == "원본유지":
        img_width = -1           # -1일때는 원본 유지
    else:
        img_width = int(img_width)

    # 간격 
    img_gap = combo_gap.get()
    if img_gap == "좁음":
        img_gap = 30
    elif img_gap == "보통":
        img_gap = 60
    elif img_gap == "넓음":
        img_gap = 90
    else:
        img_gap =0

    # 포맷
    img_format = combo_format.get().lower()      # JPG, PNG, BMP값을 받아와서 소문자로 변경

#############################################################


    images = [Image.open(x) for x in list_file.get(0, END)]     # 모든 파일목록 가져옴


    # size[0] => width  /  size[1] => height
    # widths = [x.size[0] for x in images]     # for x in images : x정의 필요하다
    # heights = [x.size[1] for x in images]
    # [(10,10), (20,30), (40,30)] 이렇게 너비, 높이 들어있었음

    img_sizes = []    # [(width1, height1), (width2, height2),...]
    if img_width > -1:          
        # width값 변경 -> height값도 변경되어야 함
        image_sizes = [ (int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

    else:
        #원본 사이즈 사용  /  [ ( , ) ] 튜플에 넣어주기
        image_sizes = [(x.size[0], x.size[1]) for x in images]   



    widths, heights = zip(*(image_sizes))            # play 폴더_zip.py 참고

    # 너비: 사진들 중 최대값, 높이: 사진들 높이 전체합
    total_width, total_heights = max(widths), sum(heights) 


    # 스케치북 준비
    if img_gap >0:     # 이미지 간격옵션 적용
        total_heights += (img_gap * (len(images)-1))

    result_img = Image.new("RGB", (total_width, total_heights), (255,255,255))
    y_offset = 0      # 사진이 아래로 차곡차곡 이어질 수 있도록 (만약 가로로 이어진 사진을 보여주고 싶다면? x_offset사용)
    # for img in images:
    #     x_middle = round((total_width - img.size[0])/2)
    #     result_img.paste(img, (x_middle, y_offset))   # y_offset= 0
    #     y_offset += img.size[1]                # y_offset에 각 사진 높이 더해줘서 바로 사진 붙여질 수 있게

    for idx, img in enumerate(images):
        # 스케치북에 img붙일때 resizing해줘야 함
        # width가 원본이 아닐때에는 width 조정해 줘야함

        if img_width > -1:
            img = img.resize(image_sizes[idx])     # .resize((225,225))

        result_img.paste(img, (0, y_offset))
        y_offset += ( img.size[1] + img_gap )      # height값 + 사용자가 지정한 간격

        progress = (idx + 1) / len(images) *100   # 실제 percent정보를 계산
        p_var.set(progress)
        progress_bar.update()
    
    '''
    result_img.paste(img, (0, y_offset)) => 사진이 중간에 위치X , x=0좌표에 붙어있어서 크기가 다른 사진들일경우
    다 왼쪽에 붙어있어서 보기가 좋지않다.
    ===> 그래서 아래와 같이 x_middle을 사용해서 사진이 중앙에 위치할 수 있도록 해주었다.
    ===> round(): 소수(예: 335.5)는 .paste의 좌표로 쓰일 수 없다고 오류가 떠서
         올림을 해서 integer(정수) 형식으로 맞춰주었다. 
    '''
    
    # 포맷옵션 처리
    file_name = "h_photo." + img_format
    save_path = os.path.join(txt_path.get(), file_name)    # h_phton.jpg 이름으로 새 경로 생성
    result_img.save(save_path)                 # 저장경로 entry에 입력된 곳에 사진 저장 
    msgbox.showinfo("알림", "작업이 완료되었습니다.")
    
# 실행
def start():
    # print(combo_width.get())
    # print(combo_gap.get())
    # print(combo_format.get())

    # 파일 목록 확인 필요!!
    if list_file.size() ==0:
        msgbox.showwarning("경고", "이미지 파일을 선택하세요.")

    # 저장경로 확인
    if len(txt_path.get()) ==0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")

    # 이미지 통합작업 : 함수 길어져서 함수는 앞에 따로 적어줄 수도 있군
    merge_image()


# 파일 프레임 (파일추가, 파일삭제 버튼 만들기)
frame_file = Frame(root)
frame_file.pack(fill="x", padx= 5, pady= 5)     # x로 펼치기

btn_addfile = Button(frame_file, padx= 5, pady= 5, width = 12, text= "파일추가", command= add_file)  
btn_addfile.pack(side="left")

btn_addfile = Button(frame_file, padx= 5, pady= 5, width = 12,text= "파일삭제", command= del_file) 
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
btn_search = Button(frame_path, width=10, text="찾아보기", command= browse_dest_path)
btn_search.pack(side= "right", padx= 5, pady= 5)


# 옵션 프레임 만들기
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
v_format= ["PNG","JPG","BMP"]
combo_format= ttk.Combobox(frame_option, values= v_format, state="readonly", width=8)
combo_format.current(0)
combo_format.pack(side= "left", padx= 5, pady= 5)


# 진행상황 progress bar

frame_progress = LabelFrame(root, text= "진행상황")
frame_progress.pack(fill="x", padx= 5, pady= 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable= p_var)
progress_bar.pack(fill="x", padx= 5, pady= 5)


# 실행 프레임 만들기
frame_run = Frame(root)
frame_run.pack(fill="x", padx= 5, pady= 5)

btn_close = Button(frame_run, padx= 5, pady= 5, width = 12,text="닫기", command= root.quit)
btn_close.pack(side="right", padx= 5, pady= 5)

btn_run = Button(frame_run, padx= 5, pady= 5, width = 12, text="시작", command= start)
btn_run.pack(side= "right", padx= 5, pady= 5)


root.resizable(False,False)  
root.mainloop()
