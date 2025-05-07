import socketserver
import datetime
from config import Config

config = Config('config.yml')
reqFile = None

# Gets the config variables
ip = config.getVar('ip')
port = config.getVar('port')
buffer_size = config.getVar('buffer_size')
log_to_file = config.getVar('log_to_file')

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        if(log_to_file):
            reqFile = open('request.txt', 'a')
            raw_data = [b'']
            while b'\n' not in raw_data[-1]:
                raw_data.append(self.request.recv(buffer_size))

            # Raw Data bytes joined into a String
            self.data = b''.join(raw_data) 

            reqFile.write(f'Received from {self.client_address[0]}, at {datetime.datetime.now()}:\n\n')
            reqFile.write(self.data.decode("utf-8"))
            reqFile.write('-'*40 + '\n')

    def finish(self):
        if(reqFile != None):
            reqFile.close()

with socketserver.TCPServer((ip, port), Handler) as server:
    server.serve_forever()