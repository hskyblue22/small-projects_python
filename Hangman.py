from random import *

words = ["calender", "book", "laptop", "pencil"]  # 리스트 요소마다 "" 해주기
word = choice(words)
print("answer : " + word)
letters =""                                       # 사용자로부터 지금까지 받은 알파벳


while True:
    succeed = True                    # succeed = True 라고 먼저 가정해 놓고 
    for w in word:
        if w in letters:              # if w in word: ==> 처음에 w가 word에 있다고 했으니 elif로 넘어가지 않는다.
            print(w, end = " ")       # 그러므로 if w in [] ==> 비어있는 변수를 넣어줘야 _ _ _ 나타낼 수 있을 듯!
    
        elif w not in letters:
            print("_", end = " ")
            succeed = False

    if succeed:
        print("\nSucceess!")
        break


    print()
    
    letter = input("알파벳을 입력하세요!")
    if letter not in letters:  # letters에 없는 letter만 추가시킨다.
        letters += letter      # letters에 letter추가시킴!!
        # print(letters)       사용자가 알파벳 입력할때마다 e , el, elb, elbt와 같이 letters에 하나씩 추가됨
    if letter in word:
        print("*딩동댕*")

    else:
        print("*땡*")
