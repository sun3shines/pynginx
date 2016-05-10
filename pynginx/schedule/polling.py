# -*- coding: utf-8 -*-

from pynginx.schedule.base import Schedule as BaseSchedule
import time
import traceback

class Schedule(BaseSchedule):
    @property
    def index(self):
        if self.lock.acquire():
            if 0 == self.length:
                self.lock.release()
                return -1
            self.i = (self.i + 1) % self.length
            self.lock.release()
            return self.i 

if __name__ == '__main__':

    s = Schedule()
    s.add(('127.0.0.1',7013))
    s.add(('127.0.0.1',7023))

    while True:
        try:
            s.get()
        except:
            # 未捕获异常，导致了线程的崩溃了。但是后台检测线程依旧在继续
            print traceback.format_exc()
        time.sleep(0.2)
                                                   
