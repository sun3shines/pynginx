import threading
import time
from pynginx.core.request import Request

class Worker(threading.Thread):
    def __init__(self,sock,addr,interval=0):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.interval = interval
    @property
    def request_class(self):
        return Request

    def run(self):
        req = self.request_class(self.sock,self.addr)
        req.process()
        if self.interval:
            time.sleep(self.interval)
 
