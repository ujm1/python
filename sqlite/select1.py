import sqlite3 #SQLite3 탑재
#전체조회용 함수

def select_all_books():
    conn=sqlite3.connect('my_books.db') #데이버테이스 커넥션 생성
    cur=conn.cursor() #커서 확보
    cur.execute('SELECT * FROM my_books') #조회용 sql 실행

    print('[1] 전체 데이터 출력하기')
    books=cur.fetchall() #조회한 데이터 불러오기
    print('books->',books)
    print('type(books)->'+type(books))

    for book in books: #데이터 출력하기
        print(book)
    conn.close()

if __name__ == '__main__': #외부에서 호출 시
    select_all_books()      #전체 조회용 함수 호출
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
