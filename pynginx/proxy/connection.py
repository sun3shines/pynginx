# -*- coding: utf-8 -*-

from pynginx.globalx.static import proxies
from pynginx.proxy.http import Request,Response

class Connection:
   
    def __init__(self,sock,addr):
        self.sock = sock
        self.addr = addr

    def handle(self):  
 
        reader = self.sock
        writer = proxies.get()
        http_method = Request(reader,writer).handle()
        Response(writer,reader,http_method).handle()
        

