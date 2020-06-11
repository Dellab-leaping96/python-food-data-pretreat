import re

# 중량 찾고 분리하는 함수
def replace(String):
    weight = ""

    if String == "":
        print("오류")

    else:
        String = String.lower()
        String_touse = String.lower()  # 모두 소문자화

        String_iter = String_touse.split()
        String_touse = ""
        for element in String_iter:
            if element.find("*") == -1 and element.find("~") and element.find("∼") == -1:
                String_touse += element + " "
        pattern = r"(([0-9]+)?(\.)?[0-9]+(m?l|k?g))"
        i = re.finditer(pattern, String_touse)  # 패턴매칭, 리스트로작성
        weight1 = []
        weight2 = []

        for element in i:
            weight += " " + element.group()

        weight1 = weight.split()
        weight_num = 0

        for element in weight1:
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
            weight2.append(element)
            weight_num = weight_num + 1

            weight_num = 0

            index = 0
            for element in weight2:
                if element == max(weight2):
                    index = weight_num
                weight_num = weight_num + 1

            if weight1:
                weight = weight1[index]

        if weight == "" and String_touse.find("kg") != -1:
            weight = "1kg"
        else:
            String = String.replace(weight, "")

    if weight == "" and String.find("kg") != -1:
        weight = "1kg"
        String = String.lower()

    return weight
