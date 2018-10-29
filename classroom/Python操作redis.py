import redis

re = redis.Redis(       #建立连接
    host = '127.0.0.1',
    port = 6379
)

# re.set('name1','nancheng')   #添加
# a = re.get('name').decode()     #获取   .decode()是解码
# print(a)

# re.expire('name',30)    #添加过期时间
# b = re.ttl('name')     #不能查看负数
# print(b)

# re.mset(a=1,b=2)    #设置多个，不是键值对
#
# re.incr('num',222)      #后面直接加参数为数量，如果不加参数默认增长1
# re.lrem('list_1',3,3)   #列表中的指定删除 后边的数字为数量 要删的元素在前边
# re.hmset('user',{'age':18,'name':'nancheng'})   #添加多个哈希值
# e = re.hmget('user','name','age')   #获取哈希值
# print(e)

#操作完结束 不用关闭连接
