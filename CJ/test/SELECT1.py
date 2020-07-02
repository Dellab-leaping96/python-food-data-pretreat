import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123123',
                       db='compdb',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM msdb'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()