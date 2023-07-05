

from car import *
car_info = getCar()
print(car_info)

import pymysql

# MySQL 서버 연결 정보
host = 'localhost'
port = 3306
user = 'human'
password = '123456'
database = 'human'          # 스키마

# MySQL 연결
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# 연결 성공 여부 확인
if connection:
    print('MySQL 연결되었습니다.')
    
# --------------------------------------------------------

print( car_info[0] )
print( car_info[1] )
print( car_info[2] )


def insertMovie( name, quantity, ranking ):
    # SQL
    sql = '''INSERT INTO car (name, quantity, ranking)
             VALUES( %s, %s, %s )
        '''
    # 데이터
    values = ( name, quantity, ranking )
    
    try:
        # 커서 생성
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            
        # 변경 사항 적용
        connection.commit()
        print('데이터 추가 완료...')
        
    except pymysql.Error as e:
        print("MySQL Error : ", e)
    
    # finally:
    # connection.close()
        


names = car_info[0]
quantitys = car_info[1]
rankings = car_info[2]

print( '국내 승용자동차 판매량 개수 : ', len(names) )

for i in range( len(names) ):
    name = names[i]
    quantity = quantitys[i]
    ranking = rankings[i]
    insertMovie( name, quantity, ranking )