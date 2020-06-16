import re

# 중량 찾고 분리하는 함수
def replace_weight(str):
    weight = ""

    if str == "":
        print("오류")

    else:
        str = str.lower()
        str_touse = str.lower()  # 모두 소문자화

        str_iter = str_touse.split()
        str_touse = ""
        for element in str_iter:
            if element.find("*") == -1 and element.find("~") and element.find("∼") == -1:
                str_touse += element + " "
        pattern = r"(([0-9]+)?(\.)?[0-9]+(m?l|k?g))"
        i = re.finditer(pattern, str_touse)  # 패턴매칭, 리스트로작성
        clause = []
        value = []

        for element in i:
            weight += " " + element.group()

        clause = weight.split()
        cnt = 0

        for element in clause:
            is_k = 0
            element = element.replace("g", "")
            element = element.replace("ml", "")

            if element.find("k") != -1 or element.find("l") != -1:
                is_k = 1
                element = element.replace("k", "")
                element = element.replace("l", "")

            element = float(element)
            if is_k == 1:
                element = int(element * 1000)
            else:
                element = int(element)
            value.append(element)
            cnt = cnt + 1

            cnt = 0

            index = 0
            for element in value:
                if element == max(value):
                    index = cnt
                cnt = cnt + 1

            if clause:
                weight = clause[index]

        if weight == "" and str_touse.find("kg") != -1:
            weight = "1kg"
        else:
            str = str.replace(weight, "")

    if weight == "" and str.find("kg") != -1:
        weight = "1kg"
        str = str.lower()

    return weight
