# 보관상태 찾는 함수
def pre(raw):
    stat = ""
    keyword = ""
    if raw.find("실온")!=-1:
        stat = "상온"
        keyword="실온"
    elif raw.find("상온")!=-1:
        stat = "상온"
        keyword = "상온"
    elif raw.find("냉장")!=-1:
        stat = "냉장"
        keyword = "냉장"
    elif raw.find("냉동")!=-1:
        stat = "냉동"
        keyword = "냉동"
    else:
        stat = "상태없음"
    return stat,keyword
