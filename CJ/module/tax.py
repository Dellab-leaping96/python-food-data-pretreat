# 면세여부 찾는 함수
def pre(raw):
    tax = ""
    keyword=""
    if raw.find("과세")!=-1:
        tax = "N"
        keyword="과세"
    elif raw.find("면세")!=-1:
        tax = "Y"
        keyword = "면세"
    else:
        tax = "상태없음"
    return tax,keyword
