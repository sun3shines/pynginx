# -*- coding: utf-8 -*-

from pynginx.core.thread.daemon import THDaemon

from pynginx.proxy.request import PRequest
from pynginx.core.thread.worker import Worker

from pynginx.globalx.static import s

class PWorker(Worker):
    @property
    def request_class(self):
        return PRequest

class Proxy(THDaemon):

    @property
    def thread_class(self):
        return PWorker

def init():

    s.put(('127.0.0.1',7011))
    s.put(('127.0.0.1',7012))
    s.put(('127.0.0.1',7013))


if __name__ == '__main__':

    init()
    Proxy('127.0.0.1',7010).run()
