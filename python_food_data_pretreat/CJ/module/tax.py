# 면세여부 찾는 함수
def find(String):
    tax = ""
    if String.find("과세")!=-1:
        tax = "N"
    elif String.find("면세")!=-1:
        tax = "Y"
    else:
        tax = "상태없음"
    return tax
