# -*- coding: utf-8 -*-

from pynginx.core.buffer.buffer import Buffer
class Request(Buffer):

    def __init__(self,reader,writer):
        self.rfile = reader.makefile('rb')
        self.wfile = writer.makefile('wb')
        self.headbuf = []
        self.bodylen = 0
        self.chunk_size = 4096

    @property
    def method(self):
        return self.headbuf[0].split()[0].strip()

    @property
    def allow(self):
        return self.bodylen

    def head(self):
        while True:
            line = self.rfile.readline()
            self.headbuf.append(line)
            if not line or '\r\n' == line:
                break
            elif line.startswith('Content-Length'):
                self.bodylen = int(line.split(':')[1].strip())
            else:
                pass

        self.wfile.write(''.join(self.headbuf))

    def body(self):
        while self.allow:
            if self.bodylen < self.chunk_size:
                self.chunk_size = self.bodylen
            chunk = self.rfile.read(self.chunk_size)
            self.wfile.write(chunk)
            self.bodylen = self.bodylen - len(chunk)

    def handle(self):
        self.head()
        self.body()
        self.close()
        return self.method

class Response(Buffer):
    def __init__(self,reader,writer,http_method):
        self.rfile = reader.makefile('rb')
        self.wfile = writer.makefile('wb')
        self._method = http_method

        self.headbuf = []
        self.bodylen = 0
        self.chunk_size = 4096

    @property
    def allow(self):
        return self._method!= 'HEAD' and self.bodylen

    def head(self):
        while True:
            line = self.rfile.readline()
            self.headbuf.append(line)
            if not line or '\r\n' == line:
                break
            elif line.startswith('Content-Length'):
                self.bodylen = int(line.split(':')[1].strip())
            elif line.startswith('Transfer-Encoding'):
                # Transfer-Encoding
                self._chunk = 'chunked' == line.split(':')[1].strip()
            else:
                pass
        self.wfile.write(''.join(self.headbuf))

    def body(self):
        if self._chunk:
            while True:
                line = self.rfile.readline()
                self.wfile.write(line)
                chunk_size = int(line.strip(),16)
                if not chunk_size:
                    self.wfile.write(self.rfile.readline())
                    break
                chunk = self.rfile.read(chunk_size)
                self.wfile.write(chunk)
                line = self.rfile.readline()
                self.wfile.write(line)
                
        else:
            while self.allow:
                if self.bodylen < self.chunk_size:
                    self.chunk_size = self.bodylen
                chunk = self.rfile.read(self.chunk_size)
                self.wfile.write(chunk)
                self.bodylen = self.bodylen - len(chunk)

