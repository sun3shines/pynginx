# -*- coding: utf-8 -*-

from pynginx.core.daemon import Daemon

from pynginx.server.request import SRequest

class Server(Daemon):

    @property
    def request_class(self):
        return SRequest


if __name__ == '__main__':

    Server('127.0.0.1',7015).run()
