import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123123',
                       db='compdb',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO msdb (code, name, det, weight, prod, tax ,stat) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, ('A0110220', '4종과일혼합', '망고,파파야,용과,파인애플', '1kg', '세미원', 'Y', '냉동'))
    conn.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
finally:
    conn.close()