#생산자명 확보가 안된 fail시트에서 키워드를 통해 생산자명 확보해주는 함수
def pre(raw, keyword_sheet):
    cnt = 2
    maker = ""
    keyword = ""
    while True:
        if keyword_sheet.cell(cnt, 1).value is None:
            break
        if raw.find(str(keyword_sheet.cell(cnt, 1).value))!=-1:
            maker = str(keyword_sheet.cell(cnt, 2).value)
            keyword = str(keyword_sheet.cell(cnt, 1).value)
            break
        cnt += 1
    return maker,keyword