import re

#생산자명추출하는 전체함수
def pre(raw,maker_sheet, nation_sheet):
    if raw.find("과세")!=-1:
        producer = maker(raw, maker_sheet)
        extra = nation(raw, nation_sheet)
    else:
        producer = nation(raw, nation_sheet)
        extra = maker(raw, maker_sheet)
    if not producer:
        producer = extra
    return producer

# 국가명 찾고 분리하는 함수
def nation(raw, nation_sheet):
    raw_touse =  re.sub('[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', raw)
    raw_iter = raw_touse.split()
    cnt = 2
    nation = ""
    while True:
        if nation_sheet.cell(cnt, 1).value is None:
            break
        for element in raw_iter:
            if element == str(nation_sheet.cell(cnt, 1).value):
                nation = str(nation_sheet.cell(cnt, 2).value)
                break
        cnt += 1
    return nation


# 제조사명 찾고 분리하는 함수
# 어절단위로만 찾음
def maker(raw, maker_sheet):
    raw_touse =  re.sub('[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', raw)
    raw_iter = raw_touse.split()
    cnt = 2
    maker = ""
    while True:
        if maker_sheet.cell(cnt, 1).value is None:
            break
        for element in raw_iter:  # 규격탭에 없을경우 상품명탭에서 한번더 국가찾기
            if element == str(maker_sheet.cell(cnt, 1).value):
                maker = str(maker_sheet.cell(cnt, 2).value)
                # break
                return maker
        cnt += 1
    return maker
