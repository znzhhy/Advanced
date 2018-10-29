import json
import os

data = {
    'name':'nancheng ',
    'age':'19',
    'li':[1,2,3],
    'tu':(11,22,33),
    'bo':True,
    'kong':None
}

json_data = json.dumps(data)

with open('json_test.json','w+') as f:
    json.dump(json_data,f)

with open('json_test.json','r') as f:
    result = json.load(f)
    print(result)

path = os.getcwd()
print('文件地址：',path)
dpath = os.path.dirname(path)
print('父级目录：',dpath)
bpath = os.path.basename(path)
print('基本短路径：',bpath)
