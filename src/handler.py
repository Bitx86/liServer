import socketserver
import datetime

#TODO Refactor the code to make it more 'clear', especially in the config.getVar sections

def make_handler(config):
    reqFile = None
    class CustomHandler(socketserver.BaseRequestHandler):
        def handle(self):
            if(config.getVar('log_to_file')):
                buffer_size = config.getVar('buffer_size')
                log_file_name = config.getVar('log_file_name')
                raw_data = [b'']

                while b'\n' not in raw_data[-1]:
                    raw_data.append(self.request.recv(buffer_size))

                # Raw Data bytes joined into a String
                self.data = b''.join(raw_data) 

                with open(log_file_name, 'a') as f:
                    f.write(f'Received from {self.client_address[0]}, at {datetime.datetime.now()}:\n\n')
                    f.write(self.data.decode("utf-8"))
                    f.write('-'*40 + '\n')
    return CustomHandler