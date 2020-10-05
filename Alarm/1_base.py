from tkinter import *
import datetime
import time
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

# timelabel 생성하기 & update_timelabel함수로 값 변경
timelabel1 = Label(root, text="", font=("Arial", 20))
timelabel1.pack()
timelabel2 = Label(root, text="", font=("Arial", 30))
timelabel2.pack()
# update_timelabel()
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