def sheet(input_sheet, output_sheet):
    ###원본데이터 열(탭)들 명시
    for i in range(1, 9):
        if input_sheet.cell(1, i).value:
            # 전처리에 사용된 열(탭)들 명시 + 단가&상품코드명시
            # 1~5열은 전처리에 사용될 문자열 / 6열은 단가 / 7열은 상품코드 / 8열은 분류로 약속해뒀음
            output_sheet.cell(1, i, str(input_sheet.cell(1, i).value))
        else:
            output_sheet.cell(1, i, "해당없음")

    ###출력데이터 열 명시
    output_sheet.cell(1, 10, "상품명")
    output_sheet.cell(1, 11, "상품설명")
    output_sheet.cell(1, 12, "중량")
    output_sheet.cell(1, 13, "생산자명")
    output_sheet.cell(1, 14, "면세여부")
    output_sheet.cell(1, 15, "상태")

def string(input_sheet,output_sheet,cnt):
    raw=""
    #1~5열 통합
    for i in range(1, 5):
        if input_sheet.cell(cnt, i).value:
            raw += str(input_sheet.cell(cnt, i).value) + " "

    #원본데이터 작성
    for i in range(1, 9):
        if input_sheet.cell(cnt, i).value:
            output_sheet.cell(cnt, i, str(input_sheet.cell(cnt, i).value))
    return raw