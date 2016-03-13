# -*- coding: utf-8 -*-

from pynginx.core.request import Request
from pynginx.core.drivers.tcp import Tcp

# server函数不可复用了。但是Tcp类可以复用了。是的。


# 需要对于conn进行封装，否则就会出现必须conn.close 的方式，而不是自由的处理了。
#　conn.close()


class Daemon:

    def __init__(self,host,port):
        self.host = host
        self.port = port

    @property
    def request_class(self):
        return Request

    def run(self):

        for conn,addr in Tcp(self.host,self.port).server():
            req = self.request_class(conn,addr)
            req.process()

