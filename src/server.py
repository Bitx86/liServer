import socketserver
from config import Config

config = Config('config.yml')

# Gets the config variables
buffer_size = config.getVar('buffer_size')
ip = config.getVar('ip')
port = config.getVar('port')

class Handler(socketserver.BaseRequestHandler):
    buffer_size = config.getVar('buffer_size')

    def handle(self):
        #print(self.request.recv(1024)) me retorna os dados enviados pelo cliente com \n
        print(self.request.recv(buffer_size))

with socketserver.TCPServer((ip, port), Handler) as server:
    server.serve_forever()