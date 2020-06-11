import re

#생산자명추출하는 전체함수
def find_all(String,tax, maker_ws, nation_ws):
    maker_1 = maker(String, maker_ws)
    maker_2 = nation(String, nation_ws)
    if not maker_1:
        maker_1 = maker_2
    return maker_1

# 국가명 찾고 분리하는 함수
def nation(String, nation_ws):
    String_touse =  re.sub('[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', String)
    String_iter = String_touse.split()
    maker_num = 2
    maker = ""
    while True:
        if nation_ws.cell(maker_num, 1).value is None:
            break
        for element in String_iter:
            if element == str(nation_ws.cell(maker_num, 1).value):
                maker = str(nation_ws.cell(maker_num, 2).value)
                break
        maker_num += 1
    return maker


# 제조사명 찾고 분리하는 함수
# 어절단위로만 찾음
def maker(String, maker_ws):
    String_touse =  re.sub('[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', String)
    String_iter = String_touse.split()
    maker_num = 2
    maker = ""
    while True:
        if maker_ws.cell(maker_num, 1).value is None:
            break
        for element in String_iter:  # 규격탭에 없을경우 상품명탭에서 한번더 국가찾기
            if element == str(maker_ws.cell(maker_num, 1).value):
                maker = str(maker_ws.cell(maker_num, 2).value)
                # break
                return maker
        maker_num += 1
    return maker
