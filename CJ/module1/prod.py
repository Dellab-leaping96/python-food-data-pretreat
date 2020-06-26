import re

#생산자명추출하는 전체함수
def pre(raw,maker_sheet, nation_sheet):
    keyword_a=""#원본에서 찾아진 값, 1군
    keyword_b=""#원본에서 찾아진 값, 2군
    producer=""#산출물에 실제로 입력될 값, 1군
    extra=""#산출물에 실제로 입력될 값, 2군
    if raw.find("과세")!=-1:
        producer,keyword_a = maker(raw, maker_sheet)
        extra,keyword_b = nation(raw, nation_sheet)
    else:
        producer,keyword_a = nation(raw, nation_sheet)
        extra,keyword_b = maker(raw, maker_sheet)
    if not producer:
        producer = extra
        keyword_a = keyword_b
    return producer, keyword_a

# 국가명 찾고 추출하는 함수
def nation(raw, nation_sheet):
    cnt = 2
    nation = ""
    keyword = ""
    while True:
        if nation_sheet.cell(cnt, 1).value is None:
            break
        if raw.find(str(nation_sheet.cell(cnt, 1).value))!=-1:
            nation = str(nation_sheet.cell(cnt, 2).value)
            keyword = str(nation_sheet.cell(cnt, 1).value)
            break
        cnt += 1
    return nation,keyword


# 제조사명 찾고 추출하는 함수
# 어절단위로만 찾음
def maker(raw, maker_sheet):
    cnt = 2
    maker = ""
    keyword = ""
    while True:
        if maker_sheet.cell(cnt, 1).value is None:
            break
        if raw.find(str(maker_sheet.cell(cnt, 1).value))!=-1:
            maker = str(maker_sheet.cell(cnt, 2).value)
            keyword = str(maker_sheet.cell(cnt, 1).value)
            break
        cnt += 1
    return maker,keyword