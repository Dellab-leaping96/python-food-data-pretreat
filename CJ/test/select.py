def MSDB_ALL(cursor):
    sql = 'SELECT * FROM msdb'
    cursor.execute(sql)
    result = cursor.fetchall()
    for element in result:
        print(element)

def CJ_ALL(cursor):
    sql = 'SELECT * FROM cj'
    cursor.execute(sql)
    result = cursor.fetchall()
    for element in result:
        print(element)