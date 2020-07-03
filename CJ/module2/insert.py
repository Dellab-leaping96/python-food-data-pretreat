#MSDB테이블 엑셀이랑 동기화
def MSDB(cursor, msdb_sheet):
    sql = 'INSERT INTO msdb (code, name, det, weight, prod, tax ,stat) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cnt = 2
    while msdb_sheet.cell(cnt, 1).value:
        code = msdb_sheet.cell(cnt, 1).value
        name = msdb_sheet.cell(cnt, 5).value
        det = msdb_sheet.cell(cnt, 6).value
        weight = msdb_sheet.cell(cnt, 7).value
        prod = msdb_sheet.cell(cnt, 8).value
        tax = msdb_sheet.cell(cnt, 9).value
        stat = msdb_sheet.cell(cnt, 10).value
        cursor.execute(sql, (code, name, det, weight, prod, tax, stat))
        cnt = cnt + 1

#CJ테이블 엑셀이랑 동기화(fail시트만)
def CJ(cursor, CJ_sheet):
    sql = 'INSERT INTO CJ (name, det, weight, prod, tax ,stat) VALUES (%s, %s, %s, %s, %s, %s)'
    cnt = 2
    while CJ_sheet.cell(cnt, 1).value:
        name = CJ_sheet.cell(cnt, 10).value
        det = CJ_sheet.cell(cnt, 11).value
        weight = CJ_sheet.cell(cnt, 12).value
        prod = CJ_sheet.cell(cnt, 13).value
        tax = CJ_sheet.cell(cnt, 14).value
        stat = CJ_sheet.cell(cnt, 15).value
        cursor.execute(sql, (name, det, weight, prod, tax, stat))
        cnt = cnt + 1