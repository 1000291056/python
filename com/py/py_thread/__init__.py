import  threading
import time
class MyThread(threading.Thread):
    "线程代码"
    lock=threading.Lock();
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        self.lock.acquire()





class Good:
    "商品类"
    count=0
    def __init__(self):
        pass
    def doSomeThing(self):
        while self.count < 100:
            print("i=", str(self.count))
