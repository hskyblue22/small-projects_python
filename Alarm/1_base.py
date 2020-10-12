from tkinter import *
import datetime
import time
import winsound
import tkinter.messagebox as msgbox 
# from datetime import datetime      # datetime 라이브러리_now함수로 현재 날짜,시간 호출 *

def th():
    t1= threading.Thread(target=set_alarm, args=())
    t1.start()

def update_timelabel():
    # 현재 날짜, 시각
    current_date = time.strftime("%Y년 %m월 %d일")
    current_time = time.strftime("%H:%M:%S")
    # timelabel 값 바꿔주기
    timelabel1.configure(text=current_date)
    timelabel2.configure(text=current_time)
    # Call the update_timeText() function after 1 second
    root.after(1000, update_timelabel)

# set버튼 클릭
def set_alarm(event):
    # hour 입력 확인
    # h = int(hourTime.get())
    if hourTime.index("end") ==0:
        msgbox.showwarning("경고","시간(hour)을 입력해주세요")         
    elif 0<= int(hourTime.get()) <=24:
        # hour.set( Done")
        pass               # return : 전체 함수 빠져나감(set_alarm빠져나가기 때문에 밑에 분,초는 검사가 안됨)
    else:
        msgbox.showwarning("경고", "시간(hour)을 정확히 입력해주세요")   

    # min 입력 확인
    m = minTime.get()
    if len(m) ==0:
        msgbox.showwarning("경고","분(min)을 입력해주세요")
    elif 0 <= int(m) <= 60 :
        # min.set(" Done")
        pass
    else:
        msgbox.showwarning("경고", "분(min)을 정확히 입력해주세요")

    # sec 입력 확인
    s = secTime.get()
    if len(s) == 0:
        msgbox.showwarning("경고","초(sec)를 입력해주세요")
    elif 0<= int(s)<=60 :
        # sec.set(" Done")
        pass
    else:
        msgbox.showwarning("경고", "초(sec)를 정확히 입력해주세요")

    if 0<=int(hourTime.get())<=24 and 0<=int(m)<=60 and 0<=int(s)<=60:
        label_var.set("Alarm has been set :)")
    else:
        label_var.set("Please check the time again.")

    user_hour= int(hourTime.get())
    user_min= int(minTime.get())
    now_hour = datetime.datetime.now().hour
    now_min= datetime.datetime.now().minute

    while user_hour != now_hour or user_min != now_min :
        now_hour = datetime.datetime.now().hour
        now_min= datetime.datetime.now().minute


    if user_hour == now_hour and user_min == now_min : 
        msgbox.showinfo("알림","It is time")  


root = Tk()
root.title("Alarm Clock")
root.geometry("430x400")

# frame_시간 설정
frame_now = Frame(root)
frame_now.pack( padx= 5, pady= 5)

# timelabel 생성하기 & update_timelabel함수로 값 변경
timelabel1 = Label(frame_now, text="", font=("Arial", 20, "bold"))
timelabel1.pack()
timelabel2 = Label(frame_now, text="", font=("Arial", 27, "bold"))
timelabel2.pack()
update_timelabel()

# 알람시간 설정 프레임
frame_set_alarm = LabelFrame(root, text="Alarm")
frame_set_alarm.pack( fill= "x", padx= 5, pady= 5, ipady= 110)

label_hour= Label(frame_set_alarm, text="hour", font=("Arial",17), fg="mediumorchid2")
label_hour.place(x=96, y=10)

label_min= Label(frame_set_alarm, text="min", font=("Arial",17), fg="mediumorchid2")
label_min.place(x=190, y=10)

label_sec= Label(frame_set_alarm, text="sec", font=("Arial",17), fg="mediumorchid2")
label_sec.place(x=279, y=10)


# 입력한 시간 초기화 할때 필요한 변수
hour = StringVar()
min = StringVar()
sec = StringVar()

# 알람 설정한 시간(사용자 입력)
hourTime= Entry(frame_set_alarm, textvariable= hour, width=8)
hourTime.place(x=90,y=43,height=35)

minTime= Entry(frame_set_alarm, textvariable = min ,width=8)
minTime.place(x=180,y=43,height=35)

secTime = Entry(frame_set_alarm, textvariable= sec, width=8)
secTime.place(x=270,y=43,height=35)

# alarm_set = Button(frame_set_alarm, text= "Set Alarm")
# alarm_set.pack(padx=5, pady=5)

# 24시간 형식 요청 레이블
label_var= StringVar()
label_var.set("Enter time in 24 hour format")

label_format= Label(frame_set_alarm, textvariable= label_var, font=("Arial",13), bg="palevioletred1",padx=2,pady=2)
label_format.place(x= 104, y=100)

# set 버튼
btn_set = Button(frame_set_alarm, text="Set",font=("Arial",15),padx=4,pady=2, width=4, command=th)
btn_set.place(x=180, y= 140)




root.mainloop()







# # 새 창 띄우기_메뉴에서 활용
# def spawn():
#     world = Toplevel()
#     world.title("New Alarm")


# x = datetime.now()
# now= x.strftime("%Y년 %m월 %d일 %H:%M:%S")
# root.title("Alarm_"+ now)       # title에 시간은 잘 나오는데 시간이 멈춰있음_title에서 시간 흐를수 있도록 하는 방법 못 찾음
                                  # 그래서 root에 날짜, 시간 나오도록 설정했음 
# root.geometry("480x320")  
# btn_new = Button(root, text="new window", command = spawn)
# btn_new.pack()
 



# root.mainloop()