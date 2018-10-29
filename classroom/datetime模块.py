import datetime

# 按照认知写
# date 日期 类
date = datetime.date(2018,8,16) #年月日，传参返回为时间格式(不可省略)
# print(date)
# print(type(date))

# time 时间 类
t = datetime.time(16,3,22)  #时分秒，可省略，省略为0
# t2 = datetime.time(16,43,22,1000)
# print(t)
# print(t2)
# print(type(t))

# datetime 日期时间 类
dt = datetime.datetime(2018,8,16,16,50,33)
# print(dt)
# print(type(dt))

# timedelta 时间间隔 类
dlt = datetime.timedelta(hours=5)
# print(dlt)
# print(dt + dlt)
# print(type(dlt))

# 当前时间
now = datetime.datetime.now()
# print(now)

# 格林威治时间
utc =  datetime.datetime.utcnow()
# print(utc)

# 东八区时间
# delt = datetime.timedelta(hours=8)
# beijing = utc + delt
# print(beijing)

# 解析时间
strp = datetime.datetime.strptime('2018-8-16 17:05:00','%Y-%m-%d %H:%M:%S')
strp2 = datetime.datetime.strptime('Aug-6-18 21:33','%b-%d-%y %H:%M')
# print(strp2)

# 格式化时间
strf = now.strftime('%Y-%m-%d %H:%M:%S')
# print(strf)

# 时间戳 从格林威治时间刚开始计算的那一刻到现在的秒数
import time
a = time.time()
print(a)
t1 = datetime.datetime.fromtimestamp(a) #时间戳转日期
print(t1)

t2 = t1.timestamp() #日期转时间戳
print(t2)



