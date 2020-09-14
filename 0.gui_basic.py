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

photo = PhotoImage(file="heart.png")
btn5 = Button(root,image = photo)
btn5.pack()


def btncmd():
    print("버튼 클릭!!")

btn6 = Button(root, text = "동작하는 버튼", command=btncmd)
btn6.pack()

root.mainloop()
