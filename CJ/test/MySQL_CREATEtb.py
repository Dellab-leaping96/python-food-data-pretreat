import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123123',
                       db='compdb',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = '''
            CREATE TABLE msdb (
                code varchar (10) NOT NULL PRIMARY KEY,
                name varchar(30) NOT NULL,
                det varchar(30) NOT NULL,
                weight varchar(5) NOT NULL,
                prod varchar(30) NOT NULL,
                tax varchar (5) NOT NULL,
                stat varchar (5) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''

        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()