import os

#print(os.name) # os模块识别操作系统 windows为'nt' 、 linux为'posix'
path = os.getcwd()  # 当前路径 /home/ubuntu/projects/home/ubuntu/projects/ketang
# print(path)
a = os.listdir()    # 当前路径下的所有内容，不添加就是相对路径
# print(a)

# os.chdir('/home/ubuntu/projects/home/ubuntu/projects/aaa')  # 改变当前路径
# b = os.getcwd()
# print(b)

# os.mkdir('nancheng')    # 创建文件夹
# os.rmdir('nancheng')    # 删除文件夹
# os.rename('nancheng','waou')    # 重命名
# f = open('nali.py','w+')    # 创建文件
# f.close()
# os.remove('nali.py')    # 删除文件

os.path.dirname(r'/home/ubuntu')    # 父级目录
os.path.basename(r'/home/ubuntu')   # 基本短路径
os.system() # 运行shell命令

# ubuntu里， reboot 重启，shutdown -h now 关机.
