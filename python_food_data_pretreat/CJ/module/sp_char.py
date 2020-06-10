import re

# 특수문자를 모두 공백으로 바꾸는 함수
def to_space(readData):
    text = re.sub(
        '[-=+,#/\?:^$.@*\"※~%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》_]', ' ', readData)
    return text
