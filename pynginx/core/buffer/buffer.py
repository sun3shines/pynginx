# -*- coding: utf-8 -*-

class Buffer:
    def __init__(self,*args,**kwargs):
        pass
 
    @property    
    def method(self):
        pass 
    
    @property
    def allow(self):
        pass

    def head(self):
        pass
    def body(self):
        pass

    def close(self):
        self.rfile.close()
        self.wfile.close()
 
    def handle(self):
        self.head()
        self.body()
        self.close()
 
