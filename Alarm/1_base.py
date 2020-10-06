from tkinter import *
import datetime
import time
import winsound
# from datetime import datetime      # datetime 라이브러리_now함수로 현재 날짜,시간 호출 *

def update_timelabel():
    # 현재 날짜, 시각
    current_date = time.strftime("%Y년 %m월 %d일")
    current_time = time.strftime("%H:%M:%S")
    # timelabel 값 바꿔주기
    timelabel1.configure(text=current_date)
    timelabel2.configure(text=current_time)
    # Call the update_timeText() function after 1 second
    root.after(1000, update_timelabel)

root = Tk()
root.title("Alarm Clock")
root.geometry("430x300")

frame_now = Frame(root)
frame_now.pack( padx= 5, pady= 5)

# timelabel 생성하기 & update_timelabel함수로 값 변경
timelabel1 = Label(frame_now, text="", font=("Arial", 20))
timelabel1.pack()
timelabel2 = Label(frame_now, text="", font=("Arial", 27))
timelabel2.pack()
update_timelabel()


frame_set_alarm = LabelFrame(root, text="Alarm")
frame_set_alarm.pack( fill= "x", padx= 5, pady= 5, ipady= 80)

# 입력한 시간 초기화 할때 필요한 변수
hour = StringVar()
min = StringVar()
sec = StringVar()

# 알람 설정한 시간(사용자 입력)
hourTime= Entry(frame_set_alarm, textvariable = hour, width=8)
# hourTime.pack(side="left", ipady=7,padx=10,pady=10)
hourTime.place(x=90,y=50,ipdy=7)
minTime= Entry(frame_set_alarm,textvariable = min,width=8)
# minTime.pack(side="left", ipady=7,padx=10,pady=10)
minTime.place(x=180,y=50)
secTime = Entry(frame_set_alarm,textvariable = sec,width=8)
# secTime.pack(side="left", ipady=7,padx=10,pady=10)
secTime.place(x=270,y=50)

# alarm_set = Button(frame_set_alarm, text= "Set Alarm")
# alarm_set.pack(padx=5, pady=5)





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