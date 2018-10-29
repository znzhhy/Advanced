import pymysql
#建立连接
conn = pymysql.connect(
    host = '127.0.0.1',     #目的主机ip
    port = 3306,   #mysql 端口 或 转发后的端口
    user = 'nancheng',    # 数据库用户名
    password = '132800',    #用户密码
    db = 'school',  #使用的数据库名
    charset = 'utf8'

)
print(conn)
#定义游标
cur = conn.cursor()

# 执行sql
row = cur.execute('show tables')
print(row)

# 取出所有数据
# all = cur.fetchall()
# print(all)    #取出元祖

# for i in all:
#     print(*i) #单个取出

#取出其中一条
# one = cur.fetchall()
# print(one)

#取出其中几条
# many = cur.fetchmany(3)
# print(*many)

#查询其他
# select = cur.execute('select * from student')
# print(select)
all2 = cur.fetchmany()
print(*all2)

#创建表格
# table = '''
# create table test11(
# id int,
# name char(10))
# '''
# cur.execute(table)

#添加数据
# cur.execute("insert test11 value(2,'小刘')")
# 注：    conn.commit()   #提交事务
#         conn.rollback()     #回滚
'''
原子性：
一致性：
隔离性：
持久性：
'''

# 进行多条操作
# cur.executemany("insert test11 value(%s,%s)",[(3,'小白'),(4,'小李')])
# conn.commit()

# 注：关闭游标
# cur.close()
#
# 注：关闭连接
# conn.close()
