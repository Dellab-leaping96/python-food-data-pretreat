import re

# 상세정보 찾고 분리하는 함수
def pre(raw, k1, k2, k3 ,k4 ,k5):

    raw_touse=raw
    if k1:
        raw_touse = raw_touse.replace(k1," ")
    if k2:
        raw_touse = raw_touse.replace(k2, " ")
    if k3:
        raw_touse = raw_touse.replace(k3, " ")
    if k4:
        raw_touse = raw_touse.replace(k4, " ")
    if k5:
        raw_touse = raw_touse.replace(k5, " ")
        raw_touse = raw_touse.replace(k5.replace("Kg", "L"), " ")
        raw_touse = raw_touse.replace(k5.replace("L", "kg"), " ")
        raw_touse = raw_touse.replace(k5.replace("ml", "g"), " ")
        raw_touse = raw_touse.replace(k5.replace("g", "ml"), " ")

    raw_touse = re.sub('[()_]', " ", raw_touse)
    raw_touse = re.sub('/((EA)|(KG)|(BOX)|(PAC))', " ", raw_touse)

    clause = raw_touse.split()
    detail = ""  # 최종 상품상세

    # 모든 상세정보리스트 종합
    for i in range(0, len(clause)):
        if i==0:
            detail = clause[0]
        else:
            detail = detail+","+clause[i]

    #if detail=="":
    #   detail ="상세정보없음"

    """
        # 단순 정보는 제거
        if clause[i] == "ea" or clause[i] == "팩" or clause[i
        ] == "곽" or clause[i] == "pet" or clause[i] == "두께" or clause[i
        ] == "/" or clause[i] == "-" or clause[i] == "기타" or clause[
            i] == "통" or clause[i] == "pac" or clause[i] == "pak" or clause[
            i] == "kg" or clause[i] == "-n" or clause[i] == "개" or clause[i
        ] == "봉" or clause[i] == "팩포장" or clause[i] == "손":
            clause[i] = ""
    """
    return detail