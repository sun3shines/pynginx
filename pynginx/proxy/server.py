# -*- coding: utf-8 -*-

from pynginx.core.server.thread import Server
from pynginx.proxy.connection import Connection
from pynginx.globalx.static import proxies

class ProxyServer(Server):

    @property
    def connection_class(self):
        return Connection

def init():
    proxies.add(('127.0.0.1',7013))
    proxies.add(('127.0.0.1',7023))
    
if __name__ == '__main__':

    init()
    ProxyServer('127.0.0.1',7090).run()
