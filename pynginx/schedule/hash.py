# -*- coding: utf-8 -*-

from pynginx.schedule.base import Schedule as BaseSchedule
import time
from pynginx.client.stream import Stream

class Schedule(BaseSchedule):
    
    def index(self,value):
        if self.lock.acquire():
            if 0 == self.length:
                self.lock.release()
                return -1
            
            return 0 

    def get(self,value):
        sock = None
        while True:
            i = self.index(value)
            while -1 == i:
                # 如果没有可用server，则会一直等待了。
                print 'wait for server'
                time.sleep(self.interval)
                i = self.index(value)
            
            host,port = self.cache[i]
            print host,port
            try:
                sock = Stream(host,port).sock
            except:
                self.delete((host,port))
                continue
            break
        return sock
    