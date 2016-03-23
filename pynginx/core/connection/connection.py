# -*- coding: utf-8 -*-

class Connection:
    def __init__(self,sock,addr):
        self.sock = sock
        self.addr = addr
        self.readsize = 4096

        self.timeout = 5

    def process(self):
        for data in self.read():
            print data
            print len(data)


    def read(self):
        while True:
            buf = self.sock.recv(self.readsize)
            if buf:
                yield buf
            else:
                break

    def writ(self,buf):
        self.sock.send(buf)

    def close(self):
        self.sock.close()

    def set_timeout(self):
        self.sock.settimeout(self.timeout)

