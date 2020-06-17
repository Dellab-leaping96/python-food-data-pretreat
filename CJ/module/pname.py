import re
from module import sp_char

def pre(raw):

    pname=""

    #CJ 작성규칙에 의거,
    #공산: 괄호 제외한 상품명 2번째 어절이 "표준 상품명"
    #농축산: 생산자가 있는경우 2번째어절, 없는경우 1번째 어절

    regex = re.compile(r'(\((.)+)')
    matchobj = regex.search(raw)
    raw_touse = raw.replace(matchobj.group(),"")
    raw_list = raw_touse.split()

    if len(raw_list)== 2:
        pname = raw_list[1] #두번째
    elif len(raw_list)== 1:
        pname = raw_list[0] #첫번째
    else:
        pname = raw_list[len(raw_list)-1] #이름이 긴 경우 가장 마지막
    return pname
