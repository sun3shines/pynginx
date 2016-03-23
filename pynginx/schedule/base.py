# -*- coding: utf-8 -*-

import time
import threading
from pynginx.client.stream import Stream
from pynginx.schedule.network import isActive

class Monitor(threading.Thread):
    def __init__(self,elm,s):
        threading.Thread.__init__(self)
        self.elm = elm
        self.host = elm[0]
        self.port = elm[1]
        self.s = s
        self.interval = 5
        
    def run(self):
        while True:
            if isActive(self.host, self.port):
                if not self.s.has(self.elm):
                    self.s.insert(self.elm)
            else:
                if self.s.has(self.elm):
                    self.s.delete(self.elm)
            time.sleep(self.interval)
    
class Schedule:

    def __init__(self):
        self.cache = []
        self.lock = threading.Lock() 
        self.i = -1 
        self.interval = 1 
        
    def insert(self,elm):
        if self.lock.acquire():
            self.cache.append(elm) 
            self.lock.release()
            print 'insert server: ',elm[0],elm[1]

    def delete(self,elm):
        if self.lock.acquire():
            self.cache.remove(elm) 
            self.lock.release()
            print 'delete server: ',elm[0],elm[1]
                    
    def has(self,elm):
        return elm in self.cache
    
    def get(self):
        while True:
            i = self.index
            while -1 == i:
                # 如果没有可用server，则会一直等待了。
                print 'wait for server'
                time.sleep(self.interval)
                i = self.index
            
            host,port = self.cache[i]
            print host,port
            try:
                sock = Stream(host,port).sock
            except:
                self.delete((host,port))
                continue
            break
 
    @property
    def length(self):
        return len(self.cache)

    def add(self,elm):
        Monitor(elm,self).start()

# index 和length的修改，是否为同一把锁？应该是的。
# 同样的资源，但是会有的不同的算法反问方式了。即为获取索引的方式了。
# 这个可以作为 schedule调度模块的基本模型了。

