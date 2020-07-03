# 외부모듈
import openpyxl
from openpyxl import load_workbook
import pymysql.cursors
import os

# 내부모듈
from CJ.module2 import dbtoxl

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123123',
                       db='compdb',
                       charset='utf8mb4')
print("mysql 연결완료, 엔터누르면 진행")
input()

try:
    with conn.cursor() as cursor:

        #4. 쿼리문 실행
        sql = """
            UPDATE cj c
            INNER JOIN msdb m ON ((m.name LIKE CONCAT('%', (SELECT SUBSTRING_INDEX(c.det, ',', 1)), '%'))
						or (m.det LIKE CONCAT('%', (SELECT SUBSTRING_INDEX(c.det, ',', 1)), '%'))
                        or (m.prod LIKE CONCAT('%', (SELECT SUBSTRING_INDEX(c.det, ',', 1)), '%')))
					and ((m.name LIKE CONCAT('%', c.name, '%')) 
						or (m.det LIKE CONCAT('%', c.name, '%')) 
						or (m.prod LIKE CONCAT('%', c.name, '%')))
                    and m.tax = c.tax
                    and m.stat = c.stat
            SET c.prod = m.prod 
            WHERE m.code Like CONCAT('%', 'P','%')
        """
        cursor.execute(sql)

        # 5. DB 업데이트                                                                 #수정사항 반영
        conn.commit()

        #6. 업데이트시킨 CJ다운로드
        dbtoxl.CJ()


finally:
    conn.close()
    print("연결 종료")