import socketserver
import logging
import time

HOST = "0.0.0.0"
PORT = 514


def setup_logger(logger_name, log_file, level=logging.INFO):
    log_setup = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log_setup.setLevel(level)
    log_setup.addHandler(file_handler)
    log_setup.addHandler(stream_handler)


setup_logger('log_router1', 'r1.log')
setup_logger('log_router2', 'r2.log')
setup_logger('log_router3', 'r3.log')
setup_logger('log_router4', 'r4.log')
setup_logger('log_router5', 'r5.log')


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = bytes.decode(self.request[0])

        if self.client_address[0] == '1.1.1.1':
            log = logging.getLogger('log_router1')
            log.info(data)
        elif self.client_address[0] == '2.2.2.2':
            log = logging.getLogger('log_router2')
            log.info(data)
        elif self.client_address[0] == '3.3.3.3':
            log = logging.getLogger('log_router3')
            log.info(data)
        elif self.client_address[0] == '4.4.4.4':
            log = logging.getLogger('log_router4')
            log.info(data)
        elif self.client_address[0] == '5.5.5.5':
            log = logging.getLogger('log_router5')
            log.info(data)


if __name__ == "__main__":
    try:
        print("**Starting Syslog server**\n")
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        time.sleep(1)
        print("**Syslog Server Started Successfully**\n")
        time.sleep(1)
        print(f"**Listening on port> {PORT}**")
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("**Ctrl+C Pressed. Shutting down the server...**\n")
        time.sleep(1)
