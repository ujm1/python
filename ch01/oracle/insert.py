import cx_Oracle
#cx-Oracle 패키지 설치해야함

dsn=cx_Oracle.makedsn("localhost",1521,"xe")
con=cx_Oracle.connect("scott","tiger",dsn)
cursor=con.cursor()

vdeptno=input('부서번호 입력:')
vdname=input('부서명 입력:')
vloc=input('위치 입력:')

cursor:execute("insert into dept values(:deptno, :dname, :loc)",
               deptno=vdeptno, dname=vdname, loc=vloc)

print('cursor.rowcount->',cursor.rowcount)
con.commit()

#Test

con.close()