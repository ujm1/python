import sqlite3

def insert_books():
    conn=sqlite3.connect('my_books.db') #데이터베이스 커넥션 생성
    cur=conn.cursor() #커서 확보
    #데이터 입력
    cur.execute("INSERT INTO my_books VALUES ('삼국지, '2024.02.28), 'A', 200, 0)")
    #데이터 입력 sql
    insert_sql = 'INSERT INTO my_books VALUES (?,?,?,?,?)'
    #튜플을 이용한 데이터 입력
    cur.execute(insert_sql, ('초한지','2024.04.27','B',584,1))
    #책의 정보를 담고 있는 튜플들의 리스트
    books=[
        ('빅데이터 마케팅', '2018.12.02','A',296,1),
        ('구글','2-14.02.10','B',526,0),
        ('아름다운노래','2017.12.12','A',248,1)
    ]

    #여러 데이터 입력
    cur.executemany(insert_sql,books)
    print("insert_books Start3...")
    conn.commit() #데이터베이스 반영
    conn.close() #데이터베이스 닫기

if __name__ == '__main__': #외부에서 호출 시
    insert_books() #데이터 입력 함수 호출