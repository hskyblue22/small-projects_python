from tkinter import *
import datetime
import time
import tkinter.messagebox as msgbox
import threading
from pygame import mixer 
import playsound                                                                                                                        
 
alarms = []
n=1

# mixer.init()

# alarm thread 실행 
def th():
    t1= threading.Thread(target=set_alarm, args=())
    t1.daemon = True
    t1.start()

# 현재시간 업데이트 하기
def update_timelabel():
    # 현재 날짜, 시각
    current_date = time.strftime("%Y/%m/%d")
    current_time = time.strftime("%H:%M:%S")
    # timelabel 값 바꿔주기
    timelabel1.configure(text=current_date)
    timelabel2.configure(text=current_time)
    # update_timelabel()함수를 1초마다 호출
    root.after(1000, update_timelabel)

def update_list():
    global alarms,n
    if 0<=int(hourTime.get())<=24 and 0<=int(minTime.get())<=60:
        alarm = "Alarm #"+ str(n) + "  " + hourTime.get()+ ":"+ minTime.get()
        alarms += [alarm]
        list_alarm.insert(END,alarm)
        n += 1
    
# 레이블 값 바꾸기
def label_change():
    if 0<=int(hourTime.get())<=24 and 0<=int(minTime.get())<=60:
        label_var.set("Alarm has been set :)")          # stringvar에는 configure속성이 없다.
    else:
        label_var.set("Please check the time again.")

# set버튼 클릭
def set_alarm():
    # hour 입력 확인
    h = hourTime.get()
    # if hourTime.index("end") ==0:       '빈 칸이다' 이렇게도 표현 가능
    if len(h) == 0:
        msgbox.showwarning("warning","Please enter the hour.")         
    elif 0<= int(hourTime.get()) <=24:
        pass               # return : 전체 함수 빠져나감(set_alarm빠져나가기 때문에 밑에 분,초는 검사가 안됨)
    else:
        msgbox.showwarning("warning", "Please check the hour again.")   

    # min 입력 확인
    m = minTime.get()
    if len(m) ==0:
        msgbox.showwarning("warning","Please enter the minute.")
    elif 0 <= int(m) <= 60 :
        pass
    else:
        msgbox.showwarning("warning", "please check the minute again.")

    label_change()

    user_hour= int(h)
    user_min= int(m)
    now_hour = datetime.datetime.now().hour
    now_min= datetime.datetime.now().minute

    update_list()
    print(alarms)

    # 알람시간과 현재시간 비교하기
    while user_hour != now_hour or user_min != now_min :
        # now_hour를 현재시간으로 계속 바꿔줌 (real time으로 바껴야지 알람시간과 비교가능!)
        now_hour = datetime.datetime.now().hour
        now_min= datetime.datetime.now().minute

    if user_hour == now_hour and user_min == now_min : 
        # mixer.music.load('sea_waves.wav')
	    # mixer.music.play()
        msg= msgbox.showinfo("Alarm Alarm","It is time")  
        # playsound.playsound('sea_waves.wav', True)
        if msg == 'ok':
            for word in alarms:
                if m in word:
                    alarms.remove(word)
                    list_alarm.delete(0,"end")
                    for alarm in alarms:
                        list_alarm.insert("end",alarm)
       # 재생시간 공부 필요


root = Tk()
# root.configure(bg="black")
root.title("Alarm Clock")
root.geometry("400x560")

# frame_시간 설정
frame_now = Frame(root)
frame_now.pack( padx= 5, pady= 5)

# timelabel 생성하기 & update_timelabel함수로 값 변경
timelabel1 = Label(frame_now, text="", font=("Arial", 26, "bold"))
timelabel1.pack()
timelabel2 = Label(frame_now, text="", font=("Arial", 27, "bold"))
timelabel2.pack()
update_timelabel()

# 알람시간 설정 프레임
frame_set_alarm = LabelFrame(root, text="Alarm")
frame_set_alarm.pack( fill= "x", padx= 5, pady= 5, ipady= 100)
# 알람시간 입력칸 위 레이블(hour,min,second)
label_hour= Label(frame_set_alarm, text="hour", font=("Arial",17), fg="mediumorchid2")
label_hour.place(x=85, y=0)
label_min= Label(frame_set_alarm, text="min", font=("Arial",17), fg="mediumorchid2")
label_min.place(x=174, y=0)
label_sec= Label(frame_set_alarm, text="sec", font=("Arial",17), fg="mediumorchid2")
label_sec.place(x=253, y=0)


# 입력한 시간 초기화 할때 필요한 변수
hour = StringVar()
min = StringVar()

# 알람시간 입력칸
hourTime= Entry(frame_set_alarm, textvariable= hour, width=8)
hourTime.place(x=80,y=39,height=34)

minTime= Entry(frame_set_alarm, textvariable = min ,width=8)
minTime.place(x=163,y=39,height=34)

secTime = Entry(frame_set_alarm, width=8)
secTime.place(x=243,y=39,height=34)
secTime.insert(END,"00")
secTime.configure(state="readonly")

# 24시간형식 입력 요청 레이블
label_var= StringVar()
label_var.set("Enter time in 24 hour format")

label_format= Label(frame_set_alarm, textvariable= label_var, font=("Arial",13), bg="palevioletred1",padx=2,pady=2)
label_format.place(x= 89, y=92)

# set 버튼
btn_set = Button(frame_set_alarm, text="Set",font=("Arial",15),padx=4,pady=2, width=4, command=th)
btn_set.place(x=160, y= 130)
# alarm_set = Button(frame_set_alarm, text= "Set Alarm")
# alarm_set.pack(padx=5, pady=5)


frame_list = Frame(root)
frame_list.pack( fill= "x", padx= 5, pady= 25, ipady= 100)

# 리스트박스
list_alarm = Listbox(frame_list, width = 50)
list_alarm.pack()



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