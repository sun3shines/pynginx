
from pynginx.common.task import Task
import pynginx.common.mission as mission

class Buffer(Task):

    def __init__(self,path):
        self.path = path

    def getUrl(self):
        return 'testUrl?aa=11'

    def getBody(self):
        return 'bodybody'

    def getHeaders(self):
        return {'md5':'111111111111'}

    def getParams(self):
        return {'path':self.path}
       

if __name__ == '__main__': 
    
    t = Buffer('/root/install.log')
    t = mission.execute('127.0.0.1',7010,t)
