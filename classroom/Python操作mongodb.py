import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1',27017)

# 获取数据库
db = client['nancheng']
# 获取集合
col = db['nancheng']

# 测试是否成功
# data = col.find()
data = col.find_one()
# print(data)

# 插入一条
# col.insert_one({'name':'yaocheng','age':18})
# 插入多条
# li = [
#     {'name':'aaa','age':18},
#     {'name':'aaa','age':15},
#     {'name':'aaa','age':52},
# ]
# col.insert_many(li)

# 更新一条数据
# col.update_one({'name':'aaa'},{'$set':{'age':22}})
# 更新多条数据
# col.update_many({'name':'aaa'},{'$set':{'age':19}})

# 删除一条数据
col.delete_one({'name':'aaa'})
# 删除多条数据
col.delete_many({'name':'aaa'})









