# -*- coding: utf-8 -*-

import socket
def isActive(host,port):
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((host,int(port)))
        sock.shutdown(2) 
        sock.close() 
        return True
    except:
        sock.close()
        return False