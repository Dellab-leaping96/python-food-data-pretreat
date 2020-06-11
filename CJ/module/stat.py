# 보관상태 찾는 함수
def find(String):
    stat = ""
    if String.find("실온")!=-1:
        stat = "상온"
    elif String.find("상온")!=-1:
        stat = "상온"
    elif String.find("냉장")!=-1:
        stat = "냉장"
    elif String.find("냉동")!=-1:
        stat = "냉동"
    else:
        stat = "상태없음"
    return stat
