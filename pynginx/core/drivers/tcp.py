# -*- coding: utf-8 -*-

import socket

class Tcp:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.idle = 600

    def client(self):
        self.socket.connect((self.host,self.port))
        return self.socket       

    def server(self):
      
        self.reuseaddr()
        self.keepalive()
        self.keepidle()
 
        self.socket.bind((self.host,self.port))
        self.socket.listen(5)
        while True:
            connection,address = self.socket.accept()
            yield connection,address
           

    def reuseaddr(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def keepalive(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    def keepidle(self):
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, self.idle)     

