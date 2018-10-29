import base64

# 方便数据进行传输，一般小段内容传输
# 编码，解码
# str = 'data'.encode()
# result = base64.b64encode(str)  #编码
# print(result)

# result = base64.b64decode(result)   #解码
# print(result)

url = 'https://www.baidu.com'.encode()
result = base64.urlsafe_b64encode(url)
print(result)
result = base64.urlsafe_b64decode(result)
print(result)