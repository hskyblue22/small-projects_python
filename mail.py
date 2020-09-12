# Quiz) 동일한 내용의 메일에 유튜버 이름 정보만 변경하여 파일로 저장하는 프로그램을 만드시오.

# [조건]
# 1. 유튜버 이름은 리스트로 제공(최소 2명 이상)
# 예) names = ["유1","유2","유3","유4"]

# 2. 파일명은 '유튜버 이름.txt' 로 저장
# 예) 나도코딩.txt, 너도코딩.txt

# [메일 본문]
# 안녕하세요? XXX님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.


names = ["선바","대도","풍월량","크림히어로즈"]

for name in names:
    with open("{0}.txt".format(name),"w",encoding = "utf8") as file_1:
        file_1.write("안녕하세요? {0}님\n".format(name))
        file_1.write("\n(주)나도출판 편집자 나코입니다.\n현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.")
        file_1.write("\n{0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.".format(name))
        file_1.write("\n자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n")
        file_1.write("\n좋은 하루 보내세요 ^^\n감사합니다.\n")
        file_1.write("\n-나코 드림.")



#=============================다른 답==================================

for n in names:
    with open("{}.txt".format(n),"w",encoding = "utf8") as email_file:
        email_file.write(f"안녕하세요? {n}님.\n\n"
                        "(주)나도출판 편집자 나코입니다.\n"
                        "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
                        f"{n}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
                        "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n"
                        "좋은 하루 보내세요 ^^\n"
                        "감사합니다.\n\n"
                        "- 나코 드림.")

#     email_file.write(f"""          
# 안녕하세요? {name}님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# {name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.    ===> 줄 안맞춘 경우, 띄어쓰기가 들쭉날쭉하다.
# """)

        