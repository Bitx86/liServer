from config import Config
from handler import make_handler
import socketserver
import socket

# TODO Resolve Server Shutdown and Error 98 'Address already in use'

config = Config('config.yml')
Handler = make_handler(config)

ip = config.getVar('ip')
port = config.getVar('port')

with socketserver.TCPServer((ip, port), Handler) as server:
    try:
        print(f'Server running at {ip}:{port}')
        server.serve_forever()

    except KeyboardInterrupt:
        print('\nStopping the server...')

    finally:
        server.server_close()
        print("Server stopped")