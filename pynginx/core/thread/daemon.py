# -*- coding: utf-8 -*-

from pynginx.core.request import Request
from pynginx.core.drivers.tcp import Tcp
from pynginx.core.thread.worker import Worker
from pynginx.core.daemon import Daemon

# server函数不可复用了。但是Tcp类可以复用了。是的。


# 需要对于conn进行封装，否则就会出现必须conn.close 的方式，而不是自由的处理了。
#　conn.close()


class THDaemon(Daemon):

    def __init__(self,host,port):
        self.host = host
        self.port = port

    @property
    def thread_class(self):
        return Worker

    def run(self):

        for conn,addr in Tcp(self.host,self.port).server():
            self.thread_class(conn,addr).run()

