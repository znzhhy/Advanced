import hashlib

# 用hashlib转换一个字符串为hash类型，加密
password = '123456'.encode('utf8')

salt = 'sfdgweg'.encode()   # 加盐
# password = '123456'.encode() + salt.encode('utf8')
# result = hashlib.new('md5',password)
#只能对字节加密 需要指定加密格式 转换后定长，且不重复
result = hashlib.md5(password)  #直接点方法更快速调用
# print(result)       #只会查看哈希对象
print(result.hexdigest())   #查看哈希对象值
# print(result.digest())      #查看哈希对象值（二进制）
hashlib.pbkdf2_hmac('md5',password,salt,10000)
#md5格式，对password加密，加盐，加密10000次   一般用来对密码进行加密
print(result)
