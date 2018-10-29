import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'nancheng',
    password = '132800',
    db = 'school',
    charset = 'utf8'
)

cur = conn.cursor()

table = '''
create table test2(
id int primary key,
name char(20) not null
)
'''
cur.execute(table)

cur.executemany("insert into test2 value(%s,%s)",[(1,'南城'),(2,'lucky'),(3,'墨染'),(4,'莉莉')])

cur.execute("delete from test2 where id = 2")

cur.execute("update test2 set id = 5 where id = 2")

select = cur.execute("select * from test2")
print(select)
a = cur.fetchall()
print(a)

conn.commit()

cur.close()
conn.close()

