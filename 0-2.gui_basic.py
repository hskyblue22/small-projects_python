from tkinter import *

root = Tk()                         
root.geometry("350x430")      

# 17, 18. 그리드
# 애플 키보드 일부분 만들기 _버튼 가로 크기 = text 길이

btn_f16= Button(root, text="F16",width = 5, height=2)
btn_f17= Button(root, text="F17",width = 5, height=2)
btn_f18= Button(root, text="F18",width = 5, height=2)
btn_f19= Button(root, text="F19",width = 5, height=2)

btn_f16.grid(row=0, column= 0, sticky= N+E+W+S, padx=3,pady=3)
btn_f17.grid(row=0, column= 1, sticky= N+E+W+S, padx=3,pady=3)
btn_f18.grid(row=0, column= 2, sticky= N+E+W+S, padx=3,pady=3)
btn_f19.grid(row=0, column= 3, sticky= N+E+W+S, padx=3,pady=3)


btn_clear= Button(root, text="Clear",width = 5, height=2)
btn_equal= Button(root, text="=",width = 5, height=2)
btn_div= Button(root, text="/",width = 5, height=2)
btn_mul= Button(root, text="*",width = 5, height=2)

btn_clear.grid(row=1, column= 0, sticky= N+E+W+S, padx=3,pady=3)
btn_equal.grid(row=1, column= 1, sticky= N+E+W+S, padx=3,pady=3)
btn_div.grid(row=1, column= 2, sticky= N+E+W+S, padx=3,pady=3)
btn_mul.grid(row=1, column= 3, sticky= N+E+W+S, padx=3,pady=3)


btn_7 = Button(root, text="7",width = 5, height=2)
btn_8 = Button(root, text="8",width = 5, height=2)
btn_9 = Button(root, text="9",width = 5, height=2)
btn_sub = Button(root, text="-",width = 5, height=2)

btn_7.grid(row=2, column= 0, sticky= N+E+W+S, padx=3,pady=3)
btn_8.grid(row=2, column= 1, sticky= N+E+W+S, padx=3,pady=3)
btn_9.grid(row=2, column= 2, sticky= N+E+W+S, padx=3,pady=3)
btn_sub.grid(row=2, column= 3, sticky= N+E+W+S, padx=3,pady=3)


btn_4 = Button(root, text="4",width = 5, height=2)
btn_5 = Button(root, text="5",width = 5, height=2)
btn_6 = Button(root, text="6",width = 5, height=2)
btn_add = Button(root, text="+",width = 5, height=2)

btn_4.grid(row=3, column= 0, sticky= N+E+W+S, padx=3,pady=3)
btn_5.grid(row=3, column= 1, sticky= N+E+W+S, padx=3,pady=3)
btn_6.grid(row=3, column= 2, sticky= N+E+W+S, padx=3,pady=3)
btn_add.grid(row=3, column= 3, sticky= N+E+W+S, padx=3,pady=3)


btn_1 = Button(root, text="1",width = 5, height=2)
btn_2 = Button(root, text="2",width = 5, height=2)
btn_3 = Button(root, text="3",width = 5, height=2)
btn_enter = Button(root, text="enter",width = 5, height=2)  

btn_1.grid(row=4, column= 0, sticky= N+E+W+S, padx=3,pady=3)
btn_2.grid(row=4, column= 1, sticky= N+E+W+S, padx=3,pady=3)
btn_3.grid(row=4, column= 2, sticky= N+E+W+S, padx=3,pady=3)
btn_enter.grid(row=4, column= 3, rowspan=2, sticky= N+E+W+S, padx=3,pady=3)         # 행 2줄 합치기


btn_0 = Button(root, text="0",width = 5, height=2)
btn_spot = Button(root, text=".",width = 5, height=2)

btn_0.grid(row=5, column= 0, columnspan=2, sticky= N+E+W+S, padx=3,pady=3)
btn_spot.grid(row=5, column= 2, sticky= N+E+W+S, padx=3,pady=3)

'''
1. grid(,sticky = N+E+W+S) : 원하는 방향으로 버튼 크기 늘리기
2. Button(,padx=10, pady=10) : 버튼 크기 늘리기(글자길이에 따라 버튼 크기 달라짐)
   ==> enter의 글자 길이가 상대적으로 길어서 enter버튼의 가로가 조금 더 길어보인다.
3. 2의 내용을 Button(,width = 5, height=2) 로 바꿔주면 길이가 고정이 된다.
   =>1) padx=10, pady=10  복사
   =>2) ctrl+f : 찾기 컨트롤에 붙이기
   =>3) 화살표 클릭해서 바꾸려는 문장 [width = 5, height=2] 입력
   =>4) replace버튼 클릭
4. grid(,padx=3,pady=3) : 버튼 사이 간격 늘리기
'''

root.mainloop()