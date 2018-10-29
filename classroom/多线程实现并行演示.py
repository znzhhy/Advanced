import time
import threading

print('外层开始',time.asctime())
def fun(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fun(n - 1) + fun(n - 2)
t = threading.Thread(target=fun,args=(35,))
t.start()
fun(35)
print('外层end',time.asctime())