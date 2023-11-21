import socketserver
import logging
from fpdf import FPDF, XPos, YPos
import time

HOST = "0.0.0.0"
PORT = 514

title = "Syslog Report"


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


class PDF(FPDF):
    def header(self):
        # logo
        self.image('Logo_del_ITESO.svg.png', 10, 8, 25)
        self.set_font('helvetica', 'B', 20)
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 10, title, border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(10)

    # page footer
    def footer(self):
        # Set position of footer
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(169, 169, 169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def router_number_title(self, r_num):
        self.set_font('helvetica', 'B', 12)
        self.set_fill_color(200, 220, 225)
        router_title = f'Router {r_num}>'
        self.ln()
        self.cell(0, 5, router_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln()

    def body(self, text):
        with open(text, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('helvetica', '', 12)
        self.ln()
        self.multi_cell(0, 8, txt, align='J')
        self.ln()

    def print_router_int(self, r_num, text):
        self.add_page()
        self.router_number_title(r_num)
        self.body(text)


# Create FPDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)


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
        print('')
        print("**Ctrl+C Pressed. Shutting down the server...**\n")
        time.sleep(1)
        print("**Creating PDF Report**\n")
        time.sleep(1)
        pdf.print_router_int(1, 'r1.log')
        pdf.print_router_int(2, 'r2.log')
        pdf.print_router_int(3, 'r3.log')
        pdf.print_router_int(4, 'r4.log')
        pdf.print_router_int(5, 'r5.log')

        pdf.output('syslog_report.pdf')
        print("**Report Created Successfully**")
        time.sleep(1)
