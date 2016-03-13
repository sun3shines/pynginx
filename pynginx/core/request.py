# -*- coding: utf-8 -*-

class Request:
    def __init__(self,sock,addr):
        self.sock = sock
        self.addr = addr
        self.readsize = 4096

        self.timeout = 5

    def process(self):
        for data in self.reader():
            print data
            print len(data)


    def reader(self):
        while True:
            buf = self.sock.recv(self.readsize)
            if buf:
                yield buf
            else:
                break

    def writer(self,buf):
        self.sock.send(buf)

    def close(self):
        self.sock.close()

    def set_timeout():
        self.sock.settimeout(self.timeout)

