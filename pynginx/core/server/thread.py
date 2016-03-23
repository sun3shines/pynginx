# -*- coding: utf-8 -*-

import threading
import time

from pynginx.core.connection.connection import Connection
from pynginx.core.drivers.tcp import Tcp
from pynginx.core.server.server import Server as BaseServer

# server函数不可复用了。但是Tcp类可以复用了。是的。
# 需要对于conn进行封装，否则就会出现必须conn.close 的方式，而不是自由的处理了。
#　conn.close()

class Worker(threading.Thread):
    def __init__(self,connection_class,sock,addr,interval=0):
        threading.Thread.__init__(self)
        
        self.sock = sock
        self.addr = addr
        self.connection_calss = connection_class

    def run(self):
        conn = self.connnection_class(self.sock,self.addr)
        conn.process()
            
class Server(BaseServer):

    def __init__(self,host,port):
        self.host = host
        self.port = port

    @property
    def thread_class(self):
        return Worker

    @property
    def connection_class(self):
        return Connection
    
    def run(self):

        for sock,addr in Tcp(self.host,self.port).server():
            self.thread_class(self.connection_class,sock,addr).start()

