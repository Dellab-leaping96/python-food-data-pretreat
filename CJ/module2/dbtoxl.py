import pymysql
import os
import openpyxl
from openpyxl import Workbook


#테이블이름 받아들여서 엑셀파일로 만드는 함수
def CJ():
    conn = pymysql.connect(host='localhost', user='root', password='123123', db='compdb', charset='utf8mb4')
    try:
        with conn.cursor() as curs:
            sql = "select * from cj"
            curs.execute(sql)
            rs = curs.fetchall()

            wb = Workbook()
            ws = wb.active

            # 첫행 입력


            # DB 모든 데이터 엑셀로
            for row in rs:
                ws.append(row)

            os.chdir('..')
            wb.save(os.getcwd()+'/output/CJ_2-2.xlsx')

    finally:
        conn.close()
        wb.close()