# -*- coding: utf-8 -*-

from pynginx.core.drivers.tcp import Tcp

class Stream:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.c = None
        self.readsize = 4096
        self.timeout = 5
        self.connect()
        self.set_timeout()
        
    def set_timeout(self):
        self.c.settimeout(self.timeout)

    def connect(self):
        self.c = Tcp(self.host,self.port).client()
   
    def close(self):
        self.c.close()
 
    def sendbody(self,body):
        if hasattr(body,'read'):
            while True:
                chunk = body.read(self.readsize)
                if chunk:
                    self.c.send(chunk)
                else:
                    break
        else:
            self.c.send(body)

if __name__ == '__main__':

    s = Stream('127.0.0.1',7010)
    s.sendbody(file('/root/install.log'))
    s.close()
    s.connect()
    s.sendbody('aaa')
    s.close()

