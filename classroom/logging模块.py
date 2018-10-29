import logging

#初始化，相当于 实例化
logger = logging.getLogger('test_log')

#设置级别
logger.setLevel(logging.DEBUG) #设置最低级别，小于它的级别都不记录

#定义Handler
    #定义控制台输出handler
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)  # error情况下才会在控制台输出，低于它的都不会再控制台输出

    #记录到文件里边
fh = logging.FileHandler('test_file.log')
fh.setLevel(logging.DEBUG)  # debug级别以上才会写入log文件里面去
#格式化
formatter = logging.Formatter(
    '时间：%(asctime),s'
    '日志级别：%(levelname)s,'
    '日志消息：%(message)s'
)
#定义格式化传到控制台文件 以规定格式显示
sh.setFormatter(formatter)  #控制台
fh.setFormatter(formatter)  #文件

#启动日志文件 添加handler到对象里去
logger.addHandler(sh)
logger.addHandler(sh)

#测试
if __name__ == '__main__':
    # logger.debug('测试中')
    # logger.info('正常运行')
    # logger.warn('警告')
    # logger.error('报错')
    # logger.critical('已经不能正常运行了')

    def fun(a):     #日志记录函数
        try:
            num = 20 / a
            logger.info(num)    #如果不报错，代表正常运行
        except Exception as e:
            logger.error(e)     #如果报错就警告
fun(0)


















