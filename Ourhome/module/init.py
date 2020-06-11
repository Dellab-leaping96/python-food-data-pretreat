def sheet(load_ws, write_ws):
    ###원본데이터 열(탭)들 명시
    for i in range(1, 9):
        if load_ws.cell(1, i).value:
            # 전처리에 사용된 열(탭)들 명시 + 단가&상품코드명시
            # 1~5열은 전처리에 사용될 문자열 / 6열은 단가 / 7열은 상품코드 / 8열은 분류로 약속해뒀음
            write_ws.cell(1, i, str(load_ws.cell(1, i).value))
        else:
            write_ws.cell(1, i, "해당없음")

    ###출력데이터 열 명시
    write_ws.cell(1, 10, "상품명")
    write_ws.cell(1, 11, "상품설명")
    write_ws.cell(1, 12, "중량")
    write_ws.cell(1, 13, "생산자명")
    write_ws.cell(1, 14, "면세여부")
    write_ws.cell(1, 15, "상태")
