# -*- coding: utf-8 -*-


#采用模的形式？

import time
import threading
from pynginx.client.stream import Stream

class Schedule:

    def __init__(self):
        self.cache = []
        self.lock = threading.Lock() 
        self.i = -1 

    def put(self,elm):
        if self.lock.acquire():
            self.cache.append(elm) 
            self.lock.release()

    def get(self):
        host,port = self.cache[self.polling_index]
        return Stream(host,port).sock
    
    @property
    def length(self):
        return len(self.cache)

    @property
    def polling_index(self):
        if self.lock.acquire():
            self.i = (self.i + 1) % self.length
            self.lock.release()
            return self.i
        
# index 和length的修改，是否为同一把锁？应该是的。
# 同样的资源，但是会有的不同的算法反问方式了。即为获取索引的方式了。
# 这个可以作为 schedule调度模块的基本模型了。

if __name__ == '__main__':

    s = Schedule()
    s.put(('127.0.0.1',7011)) 
    s.put(('127.0.0.1',7012))
    s.put(('127.0.0.1',7013))

    while True:
        print s.get()
        time.sleep(0.2)
