import socketserver



class Handler(socketserver.BaseRequestHandler):
    buffer_size = 1024



    def handle(self):
        #print(self.request.recv(1024)) me retorna os dados enviados pelo cliente com \n
        print(self.request.recv(1024))

with socketserver.TCPServer(('', 9999), Handler) as server:
    server.serve_forever()