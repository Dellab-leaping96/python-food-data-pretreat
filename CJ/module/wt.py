import re

# 중량 찾고 분리하는 함수
def pre(raw):
    keyword=""
    if raw == "":
        print("오류: 입력값 없음")
    else:

        #KG 이라는 단어가 포함되면 무조건 1kg임
        if raw.find("KG")!=-1:
            weight = "1kg"
            keyword = "KG"
            return weight,keyword

        #포함 안된경우 추출
        else:
            raw_touse = raw.lower().replace("(", " ").replace(")", " ")  # 모두 소문자화, 괄호삭제
            raw_touse = re.sub('[0-9.]+(k?g)?~[0-9.]+(k?g)', ' ', raw_touse)  # 중량추출에 이용할 어절만 선별

            weight = ""
            #정규표현식으로 중량추출 시작, 가장 큰 값을 지닌 한개만 뽑는다 (총중량)
            pattern = r"(([0-9]+)?(\.)?[0-9]+(m?l|k?g))" #ml,kg이 붙은 모든어절 선별
            matchList = re.finditer(pattern, raw_touse)  #리스트로작성(객체리스트)

            #객체리스트를 문자열 리스트로 변환(사용하기 편하게)
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


            index = 0
            cnt = 0
            #최대수치를 가진 중량값을 총중량으로 채택하여 리턴
            for element in value:
                if element == max(value):
                    index = cnt
                cnt = cnt + 1

            if clause:
                weight = clause[index]

                if weight.find("kg")!=-1:
                    keyword = weight.replace("kg","Kg")
                elif weight.find("l")!=-1 and weight.find("ml")==-1:
                    keyword = weight.replace("l","L")
                else:
                    keyword = weight

            return weight,keyword