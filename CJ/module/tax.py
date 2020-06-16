# 면세여부 찾는 함수
def pre(raw):
    tax = ""
    if raw.find("과세")!=-1:
        tax = "N"
    elif raw.find("면세")!=-1:
        tax = "Y"
    else:
        tax = "상태없음"
    return tax
