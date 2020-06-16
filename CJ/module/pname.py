from module import sp_char

def pre(raw):

    pname=""

    #CJ 작성규칙에 의거,
    #공산: 괄호 제외한 상품명 2번째 어절이 "표준 상품명"
    #농축산: 생산자가 있는경우 2번째어절, 없는경우 1번째 어절

    raw_clone = raw
    raw_clone = raw_clone.replace("("," ").replace(")"," ")

    raw_list = raw_clone.split()
    if sp_char.ident_exist(raw_list[1]):
        pname = raw_list[0]
    else:
        pname = raw_list[1]
    return pname
