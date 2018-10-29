#json是一种格式
#json数据原本不可以被Python识别，需要序列化 和 反序列化。
#json是轻量级的文本数据交换格式
#前端和后端进行数据交互，其实就是js和Python进行数据交互
#json以键值对形式存储数据 叫做json字符串
#注：json名称必须用双引号（既：""）来包括
#   值可以是双引号包括的字符串、数字、true、false、null、数组，或对象。

import json

# print(json.__all__)     #查看json模块里的所有方法。
# dumps   将Python对象转换成json对象，序列化过程

data = {
    'name':'nancheng ',
    'age':'19',
    'li':[1,2,3],       #转 数组
    'tu':(11,22,33),    #转 数组
    'bo':True,          #转为true
    'kong':None         #转为null
}

json_data = json.dumps(data)    # 序列化过程，Python --> json
# print(json_data)
# print(type(json_data))

py_di = json.loads(json_data)    # 反序列化过程，json --> Python
# print(py_di)
# print(type(py_di))

# dump.load  针对于文件操作的时候使用

# json数据，写入到文件里
#在文件里面进行序列化跟反序列化的时候需要用到dump，load
#上下文管理器

# with open('test.json','w+') as f:
#     json.dump(data,f)   #序列化的方法 python数据转换成json数据，并且存入文件f

with open('test.json','r') as f:
    json.load(f)    #反序列化 data
print(py_di)
print(type(py_di))





