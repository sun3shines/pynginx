# -*- coding: utf-8 -*-

from pynginx.schedule.base import Schedule as BaseSchedule

class Schedule(BaseSchedule):
    @property
    def index(self):
        if self.lock.acquire():
            if 0 == self.length:
                self.lock.release()
                return -1
            
            return 0 
