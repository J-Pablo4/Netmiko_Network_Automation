import socketserver
import logging

HOST = "0.0.0.0"
PORT = 514
logging.basicConfig(level=logging.INFO, format="%(message)s", filename="cisco_logs.txt", filemode="a")


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = bytes.decode(self.request[0].strip())
        # print(data)
        logging.info(data)


if __name__ == "__main__":
    try:
        print("**Starting Syslog server**")
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("**Ctrl+C Pressed. Shutting down the server...**")
