# -*- coding: utf-8 -*-

from pynginx.core.connection.connection import Connection
from pynginx.core.drivers.tcp import Tcp

# server函数不可复用了。但是Tcp类可以复用了。是的。

# 需要对于conn进行封装，否则就会出现必须conn.close 的方式，而不是自由的处理了。
#　conn.close()


class Server:

    def __init__(self,host,port):
        self.host = host
        self.port = port

    @property
    def connection_class(self):
        return Connection

    def run(self):

        for sock,addr in Tcp(self.host,self.port).server():
            conn = self.connection_class(sock,addr)
            conn.handle()

