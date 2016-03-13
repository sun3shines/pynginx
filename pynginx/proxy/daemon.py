# -*- coding: utf-8 -*-

from pynginx.core.daemon import Daemon
from pynginx.proxy.request import PRequest
from pynginx.globalx.static import s

class Proxy(Daemon):

    @property
    def request_class(self):
        return PRequest

def init():

    s.put(('127.0.0.1',7011))
    s.put(('127.0.0.1',7012))
    s.put(('127.0.0.1',7013))


if __name__ == '__main__':

    init()
    Proxy('127.0.0.1',7010).run()
