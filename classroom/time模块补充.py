# time模块补充
t = time.time()

local = time.localtime()    # 时间元祖   可以有参数，但必须为时间戳
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=20,
# tm_min=23, tm_sec=47, tm_wday=3, tm_yday=228  #一年的第几天, tm_isdst=0 #夏令时)
print(type(local))
print(local)

gm = time.gmtime()  # 格林 可选时间戳
print(gm)

asc = time.asctime(local)    #返回时间字符串   仅可选时间元祖
print('asc:',asc)

strf = time.strftime('%H-%M-%S',local)    #时间格式化    local为时间元祖
print('strf:',strf)

