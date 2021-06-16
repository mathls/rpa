"""
이상헌
과제 제출

"""

import pywinmacro as pw
import time

location1 = (38, 253) # 휴지통 위치
location2 = (97, 281) # 휴지통 비우기 위치
location3 = (1050, 546) # 항목을 완전히 삭제 파업 위치

# 바탕화면 파일들 클리어 함수
def cl_b():
   pw.key_on("window")
   pw.key_on("d")
   pw.key_off("window")
   pw.key_off("d")


# 휴지통 비우기 실행 함수
def del_file():
    pw.right_click(location1)
    pw.click(location2)
    time.sleep(3) # 천천히 보여주기
    pw.click(location3)

# 실행
cl_b()

del_file()






