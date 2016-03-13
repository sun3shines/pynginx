# -*- coding: utf-8 -*-

from pynginx.core.request import Request
from pynginx.globalx.static import s
from pynginx.client.stream import Stream

class PRequest(Request):
   
    def process(self):

        host,port = s.get()
        c = Stream(host,port)
        for data in self.reader():
            c.sendbody(data)
        print 'transmit to %s %s' % (host,port)
        c.close()

