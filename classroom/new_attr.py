
# class Base:
#     def __init__(self,food):
#         self.food = food
#         # print('这是init方法')
#
#     def __new__(cls, *args, **kwargs):  # cls类本身    重写
#         print('这是new方法')
#         # print(cls,Base)
#         instance = object.__new__(cls)
#         print('这是new方法里面的',instance)
#         return instance
#
#
# a = Base('大大大大鸡腿') # 实例化时， 进入__new__ 返回一个实例 才会进入 init
# print('这是base类的实例',a)

class Base:
    name = '123'

    def __getattr__(self, item):
        print('没有这个属性')

a = Base()
print(hasattr(a,'name'))    # 判断
print(a.__getattribute__('name'))   # 取值

setattr(a,'name','444')     # 改值
print(a.name)

delattr(Base,'name')    # 删除属性
print(Base.name)