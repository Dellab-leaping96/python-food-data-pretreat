import re

# 중량 찾고 분리하는 함수
def pre(raw):
    if raw == "":
        print("오류: 입력값 없음")
    else:
        raw_touse = raw.lower().repace("("," ").replace(")"," ")  # 모두 소문자화, 괄호삭제
        raw_clause = raw_touse.split() #어절 분리
        raw_touse ="" #중량추출에 이용할 어절만 선별
        for element in raw_clause:
            if element.find("*") == -1 and element.find("~") and element.find("∼") == -1: #곱셈 / 30~50 등은 제외
                raw_touse += element + " "

        #정규표현식으로 중량추출 시작, 가장 큰 값을 지닌 한개만 뽑는다 (총중량)
        pattern = r"(([0-9]+)?(\.)?[0-9]+(m?l|k?g))" #ml,kg이 붙은 모든어절 선별
        matchList = re.finditer(pattern, raw_touse)  #리스트로작성(객체리스트)

        #객체리스트를 문자열 리스트로 변환(사용하기 편하게)
        weight = ""
        for element in matchList:
            weight += " " + element.group()
        clause = weight.split() #실제어절 문자열 리스트

        value = [] #어절이 가진 수치값

        #어절을 한개씩 세면서 수치값 입력
        for element in clause:
            #kg은
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

            cnt = 0#어절을 한개씩 세면서 수치값 입력

            index = 0
            for element in value:
                if element == max(value):
                    index = cnt
                cnt = cnt + 1

            if clause:
                weight = clause[index]

        if weight == "" and raw_touse.find("kg") != -1:
            weight = "1kg"
        else:
            raw = raw.replace(weight, "")

    if weight == "" and raw.find("kg") != -1:
        weight = "1kg"
        raw = raw.lower()

    return weight
