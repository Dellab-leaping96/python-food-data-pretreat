#msdb테이블 생성함수
def MSDB(cursor):
    sql = '''  
                CREATE TABLE msdb (
                    code varchar (10) NOT NULL PRIMARY KEY,
                    name varchar(30) NOT NULL,
                    det varchar(50) ,
                    weight varchar(10) NOT NULL,
                    prod varchar(30) NOT NULL,
                    tax varchar (5) NOT NULL,
                    stat varchar (5) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            '''
    cursor.execute(sql)

#CJ테이블 생성함수
def CJ(cursor):
    sql = '''  
                        CREATE TABLE cj (
                            code int (10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            name varchar(30) ,
                            det varchar(50) ,
                            weight varchar(10) ,
                            prod varchar(30) ,
                            tax varchar (5) ,
                            stat varchar (5)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                    '''
    cursor.execute(sql)