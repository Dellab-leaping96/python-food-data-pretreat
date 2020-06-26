#생산자명 확보가 안된 fail시트에서 패턴으로 제조사명 확보
import re
def match(raw, cnt, output_sheet):

    maker = ""
    pattern = r"([가-힣a-zA-Z])+(상회|식품|통상|FNB|F&B|푸드)"
    matchList = re.finditer(pattern, raw)

    ptcnt = 0
    for element in matchList:
        output_sheet.cell(cnt, 16+ptcnt, element.group())
        ptcnt= ptcnt+1