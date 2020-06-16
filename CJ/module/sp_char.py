import re

# 특수문자를 모두 공백으로 바꾸는 함수
def to_space(readData):
    text = re.sub(
        '[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', readData)
    return text

def ident_exist(raw):
    pattern = re.compile('[_/*+0-9]')
    is_spchar = pattern.search(raw)
    if is_spchar: return True
    else: return False