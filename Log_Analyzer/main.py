import socketserver
import logging
import time

HOST = "0.0.0.0"
PORT = 514
logging.basicConfig(level=logging.INFO, format="%(message)s", filename="cisco_logs.log", filemode="a")


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = bytes.decode(self.request[0])

        if self.client_address[0] == '1.1.1.1':
            print(f'Client:Router 1 '+data)
        elif self.client_address[0] == '2.2.2.2':
            print(f'Client:Router 2 '+data)
        elif self.client_address[0] == '3.3.3.3':
            print(f'Client:Router 3 '+data)
        elif self.client_address[0] == '4.4.4.4':
            print(f'Client:Router 4 '+data)
        elif self.client_address[0] == '5.5.5.5':
            print(f'Client:Router 5 '+data)
        # logging.info(data)


if __name__ == "__main__":
    try:
        print("**Starting Syslog server**\n")
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        time.sleep(1)
        print("**Port Started Successfully**")
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("**Ctrl+C Pressed. Shutting down the server...**")
